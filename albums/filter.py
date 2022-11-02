from django_filters.rest_framework import FilterSet
from .models import Album
class AlbumFilter(FilterSet):
    class Meta:
        model = Album
        fields={
            'cost':['lte','gte']
        }

