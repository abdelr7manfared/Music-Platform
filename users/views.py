from telnetlib import STATUS
from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
# Create your views here.
class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class UserDetail(APIView):
    permission_classes = [IsAuthenticated|ReadOnly]
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
        

