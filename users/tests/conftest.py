from pickle import NONE
from pydoc import cli
from urllib import response
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
    response  = client.post('/authentication/login/',dict(username= 'fared',password='12345678aA'))
    token = response.data['token']
    client.credentials(HTTP_AUTHORIZATION='Token ' + token)
    return client

@pytest.fixture
def getClient(user):
    def Client(user_data=None):
        client = APIClient()
        if user_data is None:
            response  = client.post('/authentication/login/',dict(username= 'fared',password='12345678aA'))
            token = response.data['token']
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            return client,user.id
        else:
            New_user = User.objects.create_user(user_data['username'],user_data['email'],user_data['password'])
            response  = client.post('/authentication/login/',dict(username= user_data['username'],password=user_data['password'],))
            token = response.data['token']
            client.credentials(HTTP_AUTHORIZATION='Token ' + token)
            return client,New_user.id
    return Client

