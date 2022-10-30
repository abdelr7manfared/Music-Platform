from cgitb import reset
from pydoc import cli
from rest_framework import status
import pytest
from rest_framework.test import  APIClient
from artists.models import Artist
@pytest.mark.django_db
def test_get_artist_return_200(client,artist):
        response = client.get("/artists/")
        data = response.data
        assert response.status_code == status.HTTP_200_OK
        assert "Stage_name" in data[0]
        assert "Social_link_field" in data[0]
        
@pytest.mark.django_db
def test_create_artist_return_201(client):
        payload = dict(Stage_name="Dama",Social_link_field="https://www.Dama.com/artist2/")
        response = client.post("/artists/",payload)
        data = response.data
        assert response.status_code == status.HTTP_201_CREATED
        assert data['Stage_name'] == payload['Stage_name']
        assert data['Social_link_field'] == payload['Social_link_field']
        
@pytest.mark.django_db
def test_create_artist_missing_Stage_name_return_400(client):
        payload = dict(Social_link_field="https://www.Dama.com/artist2/")
        response = client.post("/artists/",payload)
        data = response.data
        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert 'Stage_name' in data
@pytest.mark.django_db
def test_create_artist_missing_Social_link_field_return_201(client):
        payload = dict(Stage_name="Dama")
        response = client.post("/artists/",payload)
        data = response.data
        assert response.status_code == status.HTTP_201_CREATED
        assert data['Stage_name'] == payload['Stage_name']
