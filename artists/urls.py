from django.urls import path
from .views import ArtistList
urlpatterns = [
    path("",ArtistList.as_view())
]
