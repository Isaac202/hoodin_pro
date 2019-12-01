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
# from django.db.models import Avg, Count, Min, Sum


class SetCoautorAquivoView(APIView):

    def post(self, request, format=None):
        file = request.POST.get('file')
        file = ArquivoRegistro.objects.filter(
            id_usuario=request.user,
            pk=file
        )
        data = {'is_valid': False}
        form = CoautoresForm(request.POST)
        if form.is_valid():
            if file.exist():
                file = file.first()
                percent = request.POST.get('percentual_obra')
                percent = Decimal(percent)
                total = file.arquivoregistro_set.annotate(
                    total_percent=Sum('book__pages')).total_percent
                if (total + percent) <= Decimal('90'):
                    coautor = form.save(commit=False)
                    coautor.documento = file
                    coautor.sava()
                    data['is_valid'] = True
                    data['delete'] = str(reverse_lazy(
                        'delete_coautor', kwargs={'pk': file.pk}))
                else:
                    data['error'] = "Limite excedido, max 90%"
        return Response(data)


class DeleteCoautorFileView(APIView):

    def post(self, request, pk, format=None):
        data = {'success': False}
        coautor = Coautores.objects.filter(pk=pk, id_usuario=request.user)
        if coautor.exists():
            coautor.delete()
            data['success'] = True
        return Response(data)
