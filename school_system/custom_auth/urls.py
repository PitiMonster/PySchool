from django.urls import path, re_path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    re_path(r'sign-in/$', views.CustomObtainAuthToken.as_view(), name='login'),
    re_path(r'sign-up/$', views.CustomRegisterView.as_view(), name='register'),
]