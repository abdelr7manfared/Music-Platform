from sre_parse import State
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Artist
from .form import ArtistForm
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ArtistSerializer
from rest_framework.generics import ListCreateAPIView        
class ArtistList(ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    # def get_queryset(self):
    #     return Artist.objects.all()
    # def get_serializer_class(self):
    #     return ArtistSerializer

    # def get_serializer_context(self):
    #     return {'request':self.request}
    # inherit from APIView
    # def get(slef,request):
    #     allAlbum = Artist.objects.all()
    #     serializers = ArtistSerializer(allAlbum,many=True,context={'request': request})
    #     return Response(serializers.data)
    # def post(self,request):
    #     serializers = ArtistSerializer(data=request.data)
    #     serializers.is_valid(raise_exception=True)
    #     serializers.save()
    #     return Response(serializers.data,status=status.HTTP_201_CREATED)
