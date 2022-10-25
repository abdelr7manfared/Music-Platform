from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from knox.views import LoginView 
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
class CreateUser(APIView):

        def post(self,request):
            serializers = RegisterSerializer(data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)


class LoginUser(LoginView):
    permission_classes = [AllowAny]
    def post(self, request):
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



