from rest_framework.test import  APIClient
from rest_framework import status
import pytest
# Create your tests here.

@pytest.fixture
def create_user(api_client):
    def register(userdata):
        api_client.post('/authentication/register/',userdata)
    return register

@pytest.mark.django_db
class TestGetUser:
    def test_if_user_is_anonymous_return_401(self,api_client,create_user):
        userdata = {
        "username": "ahmed",
        "password": "12345678aA",
        "password2": "12345678aA",
        "email": "3ASH@gmaIL.COM",
        "first_name": "sooo",
        "last_name": "yasoo",
        "bio": "lol ya bro"
        }
        userInfo = {
        "username": "ahmed",
        "password": "12345678aA",
        }
        create_user(userdata)
        api_client.post('/authentication/login/',userInfo)
        response = api_client.put('/user/1/',{'username':"hassan",'email':"sa7a@gmail.com",'bio':"3ash"})
        print(response.data)
        assert response.status_code == status.HTTP_401_UNAUTHORIZED
    def test_if_user_is_authenticated_return_200(self,api_client,create_user):
        userdata = {"username": "ahmed","password": "12345678aA","password2": "12345678aA","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
        userInfo = {"username": "ahmed","password": "12345678aA",}
        updated_data = {'username':"hassan",'email':"sa7a@gmail.com",'bio':"3ash"}
        check_data = {'id':1,'username':"hassan",'email':"sa7a@gmail.com",'bio':"3ash"}
        create_user(userdata)
        responseofLogin = api_client.post('/authentication/login/',userInfo)
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + responseofLogin.data['token'])
        response = api_client.put('/user/1/',updated_data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == check_data       
    def test_get_user_data_return_200(self,create_user,api_client):
        userdata = {
        "username": "ahmed",
        "password": "12345678aA",
        "password2": "12345678aA",
        "email": "3ASH@gmaIL.COM",
        "first_name": "sooo",
        "last_name": "yasoo",
        "bio": "lol ya bro"
        }
        updated_data = {'id':1,'username':"ahmed",'email':"3ash@gmail.com",'bio':"lol ya bro"}

        create_user(userdata)
        response = api_client.get('/user/1/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data == updated_data    
    def test_required_fields_return_400(self,api_client,create_user):
        userdata = {"username": "ahmed","password": "12345678aA","password2": "12345678aA","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
        userInfo = {"username": "ahmed","password": "12345678aA",}
        updated_data = {'email':"sa7a@gmail.com",'bio':"3ash"}
        create_user(userdata)
        responseofLogin = api_client.post('/authentication/login/',userInfo)
        api_client.credentials(HTTP_AUTHORIZATION='Token ' + responseofLogin.data['token'])
        response = api_client.put('/user/1/',updated_data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    