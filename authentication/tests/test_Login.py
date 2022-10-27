from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
class TestGetUser:
    def test_login_success_return_200(self,api_client):
        Registerdata = {"username": "ahmed","password": "12345678aA","password2": "12345678aA","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
        api_client.post('/authentication/register/',Registerdata)
        response = api_client.post('/authentication/login/',dict(username="ahmed",password= "12345678aA"))
        assert response.status_code == status.HTTP_200_OK
    def test_login_fail_return_400(self,api_client):
        response = api_client.post('/authentication/login/',dict(username="ahmed",password= "12345678aA_"))
        assert response.status_code == status.HTTP_400_BAD_REQUEST
