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
