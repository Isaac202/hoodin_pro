from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.urls import reverse_lazy
from registros.models import ArquivoRegistro
from django.shortcuts import get_object_or_404
from registros_coautores.models import Coautores
from registros_coautores.forms import CoautoresForm
from django.utils import timezone
from decimal import Decimal
# Author.objects.annotate(total_pages=Sum('book__pages'))
from django.db.models import Sum


class SetCoautorAquivoView(APIView):

    # def get(self, request, pk, format=None):
    #     file = ArquivoRegistro.objects.filter(
    #         id_usuario=request.user,
    #         pk=pk
    #     )
    #     # total = file.coautores_set.annotate(
    #     #     total_percent=Sum('book__pages')).total_percent

    def post(self, request, pk, format=None):
        file = request.POST.get('file')
        file = ArquivoRegistro.objects.filter(
            id_usuario=request.user,
            pk=file
        )
        # print(request.POST, '\n\n')
        data = {'is_valid': False}
        form = CoautoresForm(request.POST)
        if form.is_valid():
            if file.exists():
                total = Decimal("0")
                file = file.first()
                percent = request.POST.get('percentual_obra')
                percent = Decimal(percent)
                coautores = file.coautores_set.all()
                if coautores.exists():
                    total = coautores.aggregate(total=Sum('percentual_obra'))["total"]
                if  (total + percent) <= Decimal('90'):
                    coautor = form.save(commit=False)
                    coautor.arquivo = file
                    coautor.save()
                    data['is_valid'] = True
                    data['delete'] = str(reverse_lazy(
                        'delete_coautor', kwargs={'pk': coautor.pk}))
                else:
                    data['error'] = "Limite excedido, max 90%"
        return Response(data)


class DeleteCoautorFileView(APIView):

    def get(self, request, pk, format=None):
        data = {'success': False}
        coautor = Coautores.objects.filter(pk=pk, arquivo__id_usuario=request.user)
        if coautor.exists():
            coautor.delete()
            data['success'] = True
        return Response(data)
