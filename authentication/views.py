from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,LoginSerializer
from users.models import User
from rest_framework.generics import ListCreateAPIView 
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny
from knox.views import LoginView 
from knox.views import LogoutView
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
class CreateUser(ListCreateAPIView):
     queryset = User.objects.all()
     serializer_class = RegisterSerializer

class LoginUser(LoginView):
    permission_classes = (permissions.AllowAny,)
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        _,token = AuthToken.objects.create(user)
        return Response({
            'token':token,
            'user':{
                'id':user.id,
                'username':user.username,
                'email':user.email,
                'bio':user.bio
            },
        })



