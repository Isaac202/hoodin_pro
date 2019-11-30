from django.urls import path, include
from servicos.api.views import ServicoExtentionsApi
from registros.api.views import BasicUploadView, DeleteFileView,SetResumeFileView

urlpatterns = [
    path('servicos/<int:pk>', ServicoExtentionsApi.as_view()),
    path('basic-upload/', BasicUploadView.as_view(), name='base_upload'),
    path('delete-file/<int:pk>', DeleteFileView.as_view(), name='delete_file'),
    path('resume-file/<int:pk>', SetResumeFileView.as_view(), name='resume_file'),
]