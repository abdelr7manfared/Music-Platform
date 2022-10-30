from cgitb import reset
from pydoc import cli
from urllib import response
import pytest
from rest_framework import status
@pytest.mark.django_db
def test_get_albums_unauthenticated_return_200(client,album):
    response = client.get("/albums/")
    data = response.data['results']   
    assert response.status_code == status.HTTP_200_OK
    assert 'id' in data[0]
    assert 'artist' in data[0]
    assert 'Stage_name' in data[0]['artist']
    assert 'Social_link_field' in data[0]['artist']
    assert 'user' in data[0]['artist']
    assert 'name' in data[0]
    assert 'release_date' in data[0]
    assert 'cost' in data[0]
@pytest.mark.django_db
def test_create_albums_return_201(auth_client,album):
    payload=dict(name="Marwan",cost=15,release_date='2081-12-12',)
    response = auth_client.post("/albums/",payload)
    data = response.data  
    assert response.status_code == status.HTTP_201_CREATED
    assert 'id' in data
    assert 'artist' in data
    assert 'Stage_name' in data['artist']
    assert 'Social_link_field' in data['artist']
    assert 'user' in data['artist']
    assert 'name' in data
    assert 'release_date' in data
    assert 'cost' in data

@pytest.mark.django_db
def test_get_albums_unauthenticated_return_200(auth_client,album):
    response = auth_client.get("/albums/")
    data = response.data['results']   
    assert response.status_code == status.HTTP_200_OK
    assert 'id' in data[0]
    assert 'artist' in data[0]
    assert 'Stage_name' in data[0]['artist']
    assert 'Social_link_field' in data[0]['artist']
    assert 'user' in data[0]['artist']
    assert 'name' in data[0]
    assert 'release_date' in data[0]
    assert 'cost' in data[0]


@pytest.mark.django_db
def test_create_albums_unauthenticated_return_200(client,artist):
    response = client.get("/albums/")
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db

def test_create_albums_with_user_not_artist_return_403(auth_client,artist2):
    payload=dict(name="Marwan",cost=15,release_date='2081-12-12',)
    response = auth_client.post("/albums/",payload)
    data = response.data  
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert 'error' in data

@pytest.mark.django_db
def test_create_albums_unauthenticated_return_403(auth_client,user):
    payload=dict(name="Marwan",cost=15,release_date='2081-12-12',)
    response = auth_client.post("/albums/",payload)
    data = response.data  
    assert response.status_code == status.HTTP_403_FORBIDDEN
    assert 'error' in data

@pytest.mark.django_db
def test_create_album_unauthenticated(artist, client):
    payload=dict(name="Marwan",cost=15,release_date='2081-12-12',)
    response = client.post('/albums/', payload)
    data = response.data
    assert response.status_code == status.HTTP_403_FORBIDDEN

