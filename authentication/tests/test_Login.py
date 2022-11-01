from cgitb import reset
from pydoc import cli
from urllib import response
from rest_framework.test import APIClient
from rest_framework import status
import pytest

@pytest.mark.django_db
def test_login_user_return_200(user,client):
    payload = dict(username="fared",password="12345678aA")
    response = client.post("/authentication/login/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert "token" in data
    assert "user" in data
    assert data['user']['username'] == user.username
    assert data['user']['email'] == user.email
    
@pytest.mark.django_db
def test_fail_login_user_return_400(client):
    payload = dict(username="fared",password="12345678aA")
    response = client.post("/authentication/login/",payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST  
    assert "non_field_errors" in data  

@pytest.mark.django_db
def test_login_user_missing_username_return_400(client):
    payload = dict(password="12345678aA")
    response = client.post("/authentication/login/",payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST  
    assert "username" in data  
@pytest.mark.django_db
def test_login_user_missing_password_return_400(client):
    payload = dict(username="fared")
    response = client.post("/authentication/login/",payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST  
    assert "password" in data  
 