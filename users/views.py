from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import  IsAuthenticatedOrReadOnly
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class UserDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
        if not request.user.pk == pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            user = get_object_or_404(User,pk=pk) 
            serializers = UserSerializer(user)
            return Response(serializers.data,status.HTTP_200_OK)
    def put(self,request,pk):
        if not request.user.pk == pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            user = get_object_or_404(User,pk=pk) 
            serializers = UserSerializer(user,data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data,status.HTTP_200_OK)
    def patch(self,request,pk):
        if not request.user.pk == pk:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        else:
            user = get_object_or_404(User,pk=pk) 
            serializers = UserSerializer(user,data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data,status.HTTP_200_OK) 
        

