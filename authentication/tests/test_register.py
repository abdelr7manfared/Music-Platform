from rest_framework import status
import pytest

@pytest.mark.django_db
def test_register_user_return_201(client):
    payload = dict(username="faerd",email="fared@gmail.com",password="123456_",password2="123456_")  
    response = client.post('/authentication/register/',payload)
    data = response.data
    assert "username" in data
    assert "email" in data
    assert "password" in data
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert response.status_code == status.HTTP_201_CREATED
@pytest.mark.django_db
def test_register_user_missing_username_return_400(client):
    payload = dict(email="fared@gmail.com",password="123456_",password2="123456_")  
    response = client.post('/authentication/register/',payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in data
@pytest.mark.django_db
def test_register_user_missing_email_return_400(client):
    payload = dict(username="faerd",password="123456_",password2="123456_")  
    response = client.post('/authentication/register/',payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "email" in data
@pytest.mark.django_db
def test_register_user_missing_password_return_400(client):
    payload = dict(username="faerd",email="fared@gmail.com",password2="123456_")  
    response = client.post('/authentication/register/',payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password" in data
@pytest.mark.django_db
def test_register_user_missing_password2_return_400(client):
    payload = dict(username="faerd",email="fared@gmail.com",password="123456_")  
    response = client.post('/authentication/register/',payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "password2" in data
