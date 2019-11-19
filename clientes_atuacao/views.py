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
                codusuario = request.data.get('codusuario')
                codcliente = request.data.get('codcliente')
                codservico = request.data.get('codservico')
                salva_atuacao  = Clientes_Atuacao.objects.create(codcliente=codcliente, codusuario= codusuario, codservico=codservico)
                msg = "Area de atuação cadastrada com sucesso"

                return Response({'msg': msg})
            else:
                return Response({'msg': 'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)

