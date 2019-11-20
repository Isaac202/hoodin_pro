from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Clientes_Atuacao
from django.views.decorators.csrf import csrf_exempt


class CadClienteAtuacao(APIView):
    msg = ""
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                id_usuario = request.data.get('id_usuario')
                id_cliente = request.data.get('id_cliente')
                codservico = request.data.get('codservico')
                salva_atuacao  = Clientes_Atuacao.objects.create(id_cliente=id_cliente, id_usuario= id_usuario, codservico=codservico)
                msg = "Area de atuação cadastrada com sucesso"

                return Response({'msg': msg})
            else:
                return Response({'msg': 'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)

