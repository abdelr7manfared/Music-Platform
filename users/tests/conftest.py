import pytest
from collections import namedtuple
from rest_framework.test import APIClient
@pytest.fixture
def api_client():
    Registerdata = {"username": "ahmed","password": "12345678aA","password2": "12345678aA","email": "3ASH@gmaIL.COM","first_name": "sooo","last_name": "yasoo","bio": "lol ya bro"}
    Logindata = {"username": "ahmed","password": "12345678aA",}
    client = APIClient()
    client.post('/authentication/register/',Registerdata)
    response  = client.post('/authentication/login/',Logindata)
    return namedtuple("api_client", "client token")(client, response.data['token'])
