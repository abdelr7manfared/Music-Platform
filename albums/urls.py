from django.urls import path
from .views import CreateAlbum

urlpatterns = [
    path("create/",CreateAlbum.as_view())
]
