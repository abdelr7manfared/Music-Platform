import pytest
from albums.models import Album
from artists.models import Artist
from users.models import User
from rest_framework.test import APIClient

@pytest.fixture
def user():
    return User.objects.create_user('fared', 'fared@email.com', '12345678aA')
@pytest.fixture
def artist(user):
     return Artist.objects.create(Stage_name="artist1",Social_link_field= "https://www.instagram.com/artist1/",user=user)
@pytest.fixture 
def artist2(user):
    return Artist.objects.create(Stage_name="artist2",Social_link_field= "https://www.instagram.com/artist1/")
@pytest.fixture
def album(artist):
    return Album.objects.create(name='7ob fen', release_date='2028-07-14', cost=23, artist=artist, album_approved=True)
@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def auth_client(user,client):
    payload = dict(username="fared",password="12345678aA")  
    response = client.post("/authentication/login/",payload)
    token = response.data['token']
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client
