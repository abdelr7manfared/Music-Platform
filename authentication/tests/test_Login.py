from pydoc import cli
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import pytest
from users.models import User

# Create your tests here.
@pytest.mark.django_db
class TestGetUser:
    def test_login_success_return_200(self):
        client = APIClient()
        client.post('/authentication/register/',{
        "username": "ahmed",
        "password": "12345678aA",
        "password2": "12345678aA",
        "email": "3ASH@gmaIL.COM",
        "first_name": "sooo",
        "last_name": "yasoo",
        "bio": "lol ya bro"
        })
        response = client.post('/authentication/login/',dict(username="ahmed",password= "12345678aA"))
        assert response.status_code == status.HTTP_200_OK
    def test_login_fail_return_403(self):
        client = APIClient()
        response = client.post('/authentication/login/',dict(username="ahmed",password= "12345678aA_"))
        assert response.status_code == status.HTTP_400_BAD_REQUEST
