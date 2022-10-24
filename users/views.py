from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import  IsAuthenticatedOrReadOnly,IsAuthenticated,AllowAny
# Create your views here.\

class UserDetail(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    def get(self,request,pk):
        user = get_object_or_404(User,pk=pk) 
        serializers = UserSerializer(user)
        return Response(serializers.data)
    def put(self,request,pk):
            user = get_object_or_404(User,pk=pk) 
            serializers = UserSerializer(user,data=request.data)
            serializers.is_valid(raise_exception=True)
            serializers.save()
            return Response(serializers.data)
        

