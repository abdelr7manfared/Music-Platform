from rest_framework.test import  APIClient
from rest_framework import status
import pytest
from rest_framework.authtoken.models import Token
from users.models import User

# Create your tests here.


@pytest.mark.django_db
class TestGetUser:
    def test_if_user_is_anonymous_return_401(self,api_client):
        response = api_client.client.put('/user/1/',{'username':"hassan",'email':"sa7a@gmail.com",'bio':"3ash"})
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    def test_if_user_is_authenticated_return_200(self,api_client):
        api_client.client.credentials(HTTP_AUTHORIZATION='Token ' + api_client.token)
        response = api_client.client.put('/user/1/',{'username':"ahmed",'email':"3ash@gmail.com",'bio':"lol ya bro"})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['username'] == "ahmed"
    def test_get_user_data_return_200(self,api_client):
        response = api_client.client.get('/user/1/')
        assert response.status_code == status.HTTP_200_OK
    def test_required_fields_return_400(self,api_client):
        api_client.client.credentials(HTTP_AUTHORIZATION='Token ' + api_client.token)
        response = api_client.client.put('/user/1/',{'email':"sa7a@gmail.com",'bio':"3ash"})
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    