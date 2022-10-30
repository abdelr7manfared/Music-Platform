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
class Aproved_Album(generics.ListAPIView):
    queryset = Album.objects.filter(album_approved__exact=True)
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination
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
        if request.user.is_authenticated:
            if  Artist.objects.filter(user__id = request.user.id).exists():
                artist = Artist.objects.get(user__id = request.user.id)
                Art = Artist(id=artist.id,Stage_name=artist.Stage_name)
                serializers = AlbumSerializer(data=request.data,context={'request': request})
                serializers.is_valid(raise_exception=True)
                serializers.save(artist=Art)
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            else:
             return Response({'error':'the user must be artist'},status = status.HTTP_403_FORBIDDEN)
        else :
            return Response({'error':'the user must be artist'},status = status.HTTP_403_FORBIDDEN)
    
class Aproved_Album_ManuallyFilter(generics.ListAPIView):
    serializer_class = AlbumSerializer
    pagination_class = LimitOffsetPagination
    def get_queryset(self):
        query = Album.objects.filter(album_approved__exact=True)
        try:
            cost_Max = self.request.query_params.get('cost__lte')
            if cost_Max is not None:
                cost_Max = int(cost_Max)        
                query = query.filter(cost__lte = cost_Max)
        except (ValueError, TypeError):
            raise ValidationErr("cost_Max Must be intger")        
        try:
            cost_Min = self.request.query_params.get('cost__gte')
            if cost_Min is not None:
                cost_Min = int(cost_Min)
                query = query.filter(cost__gte = cost_Min)
        except (ValueError, TypeError):
            raise ValidationErr("cost_Min Must be intger")
        name = self.request.query_params.get('name')
        print(name)
        if name is not None:
            query = query.filter(name__icontains = name)
        return query

    def get(self,request):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        result = self.get_paginated_response(serializer.data)
        data = result.data # pagination data
        return Response(data,status=status.HTTP_200_OK)
    def post(self,request):
        if request.user.is_authenticated:
            if  Artist.objects.filter(user__id = request.user.id).exists():
                artist = Artist.objects.get(user__id = request.user.id)
                Art = Artist(id=artist.id,Stage_name=artist.Stage_name)
                serializers = AlbumSerializer(data=request.data,context={'request': request})
                serializers.is_valid(raise_exception=True)
                serializers.save(artist=Art)
                return Response(serializers.data,status=status.HTTP_201_CREATED)
            else:
             return Response({'error':'the user must be artist'},status = status.HTTP_403_FORBIDDEN)
        else :
            return Response({'error':'the user must be artist'},status = status.HTTP_403_FORBIDDEN)
    