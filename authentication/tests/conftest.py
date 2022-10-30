import pytest
from rest_framework.test import APIClient
from users.models import User
@pytest.fixture
def user():
    return User.objects.create_user('fared', 'fared@email.com', '12345678aA')
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


