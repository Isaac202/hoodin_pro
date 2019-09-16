from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from home.views import sair
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', sair, name='logout'),
]
