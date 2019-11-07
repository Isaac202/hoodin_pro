from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import gerar_token_cartao,  comprar_credito
from django.views.decorators.csrf import csrf_exempt


class PagamentosCielo(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                msg = comprar_credito(request.data.get('id_usuario'), request.data.get('id_compra'),
                                                          request.data.get('cliente'), request.data.get('numero_cartao'),
                                                          request.data.get('seguranca'), request.data.get('bandeira'),
                                                          request.data.get('validade'), request.data.get('valor'),
                                                          request.data.get('qtd_parcela'))

                return Response({'msg': msg})
            else:
                return Response({'msg': 'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)


class CriarTokenCielo(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                tk_cartao = gerar_token_cartao(request.data.get('cliente'),
                                           request.data.get('numero_cartao'), request.data.get('seguranca'),
                                           request.data.get('bandeira'), request.data.get('validade'))

                return Response({'tkcartao': tk_cartao})
            else:
                return Response({'msg':'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)



class ComprarComToken(APIView):
    @csrf_exempt
    def post(self, request):
        try:
            if request.method == 'POST':
                msg, transacao = comprar_com_token(request.data.get('id_compra'), request.data.get('cliente'),
                                           request.data.get('numero_cartao_tk'), request.data.get('seguranca'),
                                           request.data.get('bandeira'), request.data.get('validade'),
                                           request.data.get('valor'), request.data.get('qtd_parcela'))

                return Response({'msg': msg, 'trasacao': transacao})
            else:
                return Response({'msg':'nao foi post'})

        except Exception as e:
            return Response({'erro': str(e)}, status=401)



class GerarTokenSocial(APIView):
    @csrf_exempt
    def post(self, request):
        result = None
        try:
            if request.method == 'POST':
               result = criar_token_senha(request.data.get('email'), request.data.get('senha'))
               return Response({'result':result})
        except Exception as e:
            return Response({'erro': str(e)}, status=401)

