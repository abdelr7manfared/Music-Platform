from django.urls import path
from .views import CreateArtist,ArtistList
urlpatterns = [
    path("create/",CreateArtist.as_view()),
    path("",ArtistList.as_view())
]
