from django.urls import path, include
from servicos.api.views import ServicoExtentionsApi
from registros.api.views import BasicUploadView, DeleteFileView, SetResumeFileView, VeryCredit
from registros_coautores.api.views import SetCoautorAquivoView, DeleteCoautorFileView

urlpatterns = [
    path('servicos/<int:pk>', ServicoExtentionsApi.as_view()),
    path('basic-upload/', BasicUploadView.as_view(), name='base_upload'),
    path('very-credit/', VeryCredit.as_view(), name='check'),
    path('delete-file/<int:pk>', DeleteFileView.as_view(), name='delete_file'),
    path('resume-file/<int:pk>', SetResumeFileView.as_view(), name='resume_file'),
    path('coautor-file/<int:pk>', SetCoautorAquivoView.as_view(), name='resume_file'),
    path('delete-coautor/<int:pk>',
         DeleteCoautorFileView.as_view(), name='delete_coautor'),
]
