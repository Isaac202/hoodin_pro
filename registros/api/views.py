from random import randint
from compras.models import Compras
from cielo.tasks import comprar_credito
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from registros.models import Registros, ArquivoRegistro
from registros.forms import RegistrosForm, RegistrosViewForm, ArquivoRegistroForm
from registros.api.serializers import ArquivoSerializer
from tools.genereteKey import get_size_file, file_to_shar256
from servicos.models import Servicos
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal


class BasicUploadView(APIView):
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    # def get(self, request, format=None):
        # data = {}
        # url = str(reverse_lazy('delete_file', kwargs={'pk':1}))
        # print(url)
        # data['url'] = url
        # request.session['files'].append(1)
        # data = request.session['files']
        # return Response(data)

    def post(self, request, format=None):
        service = request.GET.get('service')
        service = get_object_or_404(Servicos, pk=service)
        # cliente = request.user.clientes
        file = request.FILES['file']
        data = {'is_valid': False}
        name = file.name
        shar256 = file_to_shar256(file)
        size = file.size
        form = ArquivoRegistroForm(request.POST, request.FILES)
        old_file = ArquivoRegistro.objects.filter(name=name, id_usuario=request.user).last()
        if form.is_valid():
            file = form.save(commit=False)
            file.id_usuario = request.user
            file.shar256 = shar256
            file.name = name
            file.size = size
            file.value = service.preco
            if old_file:
                file.version = old_file.version + Decimal('1.0')
            file.save()
            serializer = ArquivoSerializer(file, many=False)
            data = serializer.data
            data['delete'] = str(reverse_lazy(
                'delete_file', kwargs={'pk': file.pk}))
            data['is_valid'] = True

        files = ArquivoRegistro.objects.filter(
            id_usuario=request.user, paid=False
        )

        price = service.preco * files.count()
        data['price'] = price
        return Response(data)


class SetResumeFileView(APIView):
    
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk, format=None):
        data = {'success': False}
        file = ArquivoRegistro.objects.filter(pk=pk, id_usuario=request.user)
        if file.exists():
            file.update(resume=request.POST['resume'])
            # file.resume =
            # file.save()
            data['success'] = True
        return Response(data)



class DeleteFileView(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def post(self, request, pk, format=None):
        data = {'success': False}
        file = ArquivoRegistro.objects.filter(pk=pk, id_usuario=request.user)
        if file.exists():
            file = file.first()
            file.file.delete()
            file.delete()
            value = ArquivoRegistro.objects.filter(
                paid=False,
                id_usuario=request.user).aggregate(total=Sum('value'))["total"]
            if value:
                value = "%.2f" % value
                data['price'] = value.replace('.',',')
            else:
                data['price'] = '0,00'
            data['success'] = True
        return Response(data)


class VeryCredit(APIView):

    def get(self, request, format=None):
        data = {}
        data['result'] = False
        data['cielo'] = False
        service = request.GET.get('service', None)
        if service:
            service = get_object_or_404(Servicos, pk=service)
            cliente = request.user.clientes
            files = ArquivoRegistro.objects.filter(
                id_usuario=request.user, paid=False
            )
            if files:
                total = service.preco * files.count()
                cliente = request.user.clientes
                if cliente.valor_credito >= total:
                    data['result'] = True
                else:
                    value = total - cliente.valor_credito
                    value = "{}".format(value).replace('.', ',')
                    # if value > Decimal('0.99'):
                    data['value'] = value
                    data['cielo'] = True
                    data['error'] = "Saldo insuficiente"
        else:
            data['error'] = 'serviço não encontrado'

        return Response(data)


class BuyCredit(APIView):

    def post(self, request, format=None):
        cliente = request.user.clientes
        nome_cartao = request.POST.get("nome_cartao")
        numero_cartao = request.POST.get("numero_cartao")
        seguranca = request.POST.get("seguranca")
        bandeira = request.POST.get("bandeira")
        validade = request.POST.get("validade")
        valor = request.POST.get("valor")
        qtd = request.POST.get('qtd_parcela', 1)
        try:
            val_decimail = Decimal(valor)
        except:
            valor = valor.replace('.', '')
            valor = valor.replace(',', '.')
            val_decimail = Decimal(valor)
        val = int(val_decimail * 100)
        pedido = randint(1, 1000000)
        data = comprar_credito(
            10, nome_cartao, numero_cartao, seguranca, bandeira, validade, val, 1)
        resposta_cielo, trasacao, codigo_compra = data

        # resp = status.HTTP_400_BAD_REQUEST
        autorizado = False
        if resposta_cielo in "Transacao autorizada":
            # resp = status.HTTP_201_CREATED
            autorizado = True
            cliente.valor_credito += val_decimail
            cliente.save()

        compra = Compras.objects.create(
            id_usuario=request.user,
            id_cliente=cliente,
            valor=val_decimail,
            codigo_compra_cielo=codigo_compra,
            transacao_cielo=trasacao
        )

        print(resposta_cielo, '\n\n')
        # , status=resp)
        return Response({'msg': resposta_cielo, 'result': autorizado})
