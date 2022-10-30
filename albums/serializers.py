
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
import artists
from django.shortcuts import get_object_or_404
from .models import Album
from artists.serializers import ArtistSerializer
from artists.models import Artist
class AlbumSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer(read_only=True)
    class Meta:
        model = Album
        fields=['id','artist','name','release_date','cost',]
