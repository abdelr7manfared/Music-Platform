from rest_framework.test import APITestCase, APIClient
from rest_framework import status
import pytest
from users.models import User
from django.urls import reverse
from rest_framework.test import RequestsClient

# Create your tests here.
@pytest.mark.django_db
class TestGetUser(APITestCase):
    @pytest.mark.skip
    def test_register(self):
        client = APIClient()
        data = {
        "username": "ahmed",
        "password": "12345678aA",
        "password2": "12345678aA",
        "email": "3ASH@gmaIL.COM",
        "first_name": "sooo",
        "last_name": "yasoo",
        "bio": "lol ya bro"
        }
        response = client.post('/authentication/register/',data)
        self.assertEqual(response.status_code , 201)
    