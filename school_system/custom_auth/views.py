from django.shortcuts import render
from user.models import User as MyUser
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_auth.registration.views import RegisterView


class CustomObtainAuthToken(ObtainAuthToken):
    ''' 
    override default class to get current logging user id
    body template must follow this template:
    username: email
    password: password
    returned token and user_id
    '''
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'user_id': token.user_id})


class CustomRegisterView(RegisterView):

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return response