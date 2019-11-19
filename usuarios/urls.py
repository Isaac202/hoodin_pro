from django.urls import re_path, path, include
from django.contrib.auth.views import LogoutView
from usuarios.views import email_enviado, confUser, login_redirect, CustonLoginView

app_name = "users"

urlpatterns = [
    path('login/', CustonLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    # path('', include('django.contrib.auth.urls')),
    path('users/redirect/', login_redirect, name='redirect'),
    path('users/confirme-o-email/', email_enviado, name='email_enviado'),
    re_path(r'^users/conf/(?P<key>[\w-]+)/$', confUser, name="conf") 
]
