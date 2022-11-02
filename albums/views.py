from sre_compile import isstring
from xml.dom import ValidationErr
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework import status
from rest_framework import generics        
from .serializers import AlbumSerializer
from .models import Album
from .filter import AlbumFilter
from artists.models import Artist
from .permissions import IsArtistPermission
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class Aproved_Album(generics.ListAPIView):
    queryset = Album.objects.filter(album_approved__exact=True)
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = [IsAuthenticatedOrReadOnly,IsArtistPermission]
    filter_backends = [DjangoFilterBackend,SearchFilter]
    filterset_class = AlbumFilter
    search_fields=['name']

    def get(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        result = self.get_paginated_response(serializer.data)
        data = result.data
        return Response(data,status=status.HTTP_200_OK)
    def post(self,request):
        artist = Artist.objects.get(user__id = request.user.id)
        Art = Artist(id=artist.id,Stage_name=artist.Stage_name)
        serializers = AlbumSerializer(data=request.data,context={'request': request})
        serializers.is_valid(raise_exception=True)
        serializers.save(artist=Art)
        return Response(serializers.data,status=status.HTTP_201_CREATED)
    
class Aproved_Album_ManuallyFilter(generics.ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        query = Album.objects.filter(album_approved__exact=True)
        try:
            cost__lte = self.request.query_params.get('cost__lte')
            if cost__lte is not None:
                cost__lte = int(cost__lte)        
                query = query.filter(cost__lte = cost__lte)
        except (ValueError, TypeError):
            raise ValidationErr("cost__lte Must be intger")        
        try:
            cost__gte = self.request.query_params.get('cost__gte')
            if cost__gte is not None:
                cost__gte = int(cost__gte)
                query = query.filter(cost__gte = cost__gte)
        except (ValueError, TypeError):
            raise ValidationErr("cost__gte Must be intger")
        name = self.request.query_params.get('name')
        if name is not None:
            query = query.filter(name__icontains = name)
        return query
