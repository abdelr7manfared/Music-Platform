from rest_framework.test import  APIClient
from rest_framework import status
import pytest

# Create your tests here.
@pytest.mark.django_db
class TestGetUser:
    def test_register(self,api_client):
        data = {"username": "ahmed","password": "12345678aA","password2": "12345678aA","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
        response = api_client.post('/authentication/register/',data)
        assert response.status_code == status.HTTP_201_CREATED
    def test_register_wrong_password(self,api_client):
        data = {"username": "ahmed","password": "12345678aA","password2": "12345678a","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
        response = api_client.post('/authentication/register/',data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST

