from cgitb import reset
from pydoc import cli
from rest_framework import status
import pytest
from rest_framework.test import  APIClient
from artists.models import Artist
@pytest.mark.django_db
class TestArtist:
    def test_get_artist_return_200(self,api_client):
        response = api_client.get("/artists/")
        assert response.status_code == status.HTTP_200_OK
    def test_create_artist_return_201(self,api_client):
        response = api_client.post("/artists/",{"Stage_name":"Dama","Social_link_field":"https://www.Dama.com/artist2/"})
        assert response.status_code == status.HTTP_201_CREATED
    def test_required_fields_return_400(self,api_client):
        response = api_client.post("/artists/",{"Social_link_field":"https://www.Dama.com/artist2/"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST