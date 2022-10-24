from cgitb import reset
from pydoc import cli
from rest_framework import status
import pytest
from rest_framework.test import  APIClient
from artists.models import Artist
@pytest.mark.django_db
class TestArtist:
    def test_get_artist_return_200(self):
        data = [
            {
                "id":1,"Stage_name":"artist1","Social_link_field":"https://www.instagram.com/artist1/"
            },
            {
                "id":2,"Stage_name":"artist2","Social_link_field":"https://www.instagram.com/artist2/"
            }
        ]
        Artist.objects.create(Stage_name="artist1",Social_link_field= "https://www.instagram.com/artist1/")
        Artist.objects.create(Stage_name="artist2",Social_link_field= "https://www.instagram.com/artist2/")
        client = APIClient()
        response = client.get("/artists/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data == data
    def test_create_artist_return_201(self):
        client = APIClient()
        artist_info = {
            "Stage_name":"Dama",
            "Social_link_field":"https://www.Dama.com/artist2/"
        }
        artist_data = {
            "id":1,
            "Stage_name":"Dama",
            "Social_link_field":"https://www.Dama.com/artist2/"
        }
        response = client.post("/artists/",artist_info)
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data == artist_data
    def test_required_fields_return_400(self):
        client = APIClient()
        artist = {
            "Social_link_field":"https://www.Dama.com/artist2/"
        }
        response = client.post("/artists/",artist)
        assert response.status_code == status.HTTP_400_BAD_REQUEST