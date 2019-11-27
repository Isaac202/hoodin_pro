from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from servicos.api.serializers import ServiceExtentionSerializer
from servicos.models import Servicos

class ServicoExtentionsApi(APIView):

    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, pk, format=None):
        s = Servicos.objects.get(pk=pk)
        serializer = ServiceExtentionSerializer(s, many=False)
        return Response(serializer.data)
