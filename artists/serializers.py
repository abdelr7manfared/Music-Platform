from pyexpat import model
from rest_framework import serializers
from artists.models import Artist
class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields='__all__'