from rest_framework import status
import pytest

@pytest.mark.django_db
def test_get_user_return_200(auth_client):
    response = auth_client.get("/user/1/")
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert "username" in data
    assert "id" in data
    assert "email" in data
    assert "bio" in data
@pytest.mark.django_db
def test_update_user_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",email="ali@gmail.com",bio="LOLyangm")
    response = cleint.put(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert "id" in data
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert data['bio'] == payload['bio']
@pytest.mark.django_db
def test_update_user_missing_username_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(email="ali@gmail.com",bio="LOLyangm")
    response = cleint.put(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in data

@pytest.mark.django_db
def test_update_user_missing_email_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",bio="LOLyangm")
    response = cleint.put(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert data['username'] == payload['username']
    assert data['bio'] == payload['bio']
        

@pytest.mark.django_db
def test_update_user_missing_bio_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",email="ali@gmail.com")
    response = cleint.put(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
        
@pytest.mark.django_db
def test_partial_update_user_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",email="ali@gmail.com",bio="LOLyangm")
    response = cleint.patch(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert "id" in data
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
    assert data['bio'] == payload['bio']
@pytest.mark.django_db
def test_partial_update_user_missing_username_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(email="ali@gmail.com",bio="LOLyangm")
    response = cleint.patch(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    assert "username" in data

@pytest.mark.django_db
def test_partial_update_user_missing_email_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",bio="LOLyangm")
    response = cleint.patch(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert data['username'] == payload['username']
    assert data['bio'] == payload['bio']
        

@pytest.mark.django_db
def test_partial_update_user_missing_bio_return_200(getClient):
    cleint,id = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",email="ali@gmail.com")
    response = cleint.patch(f"/user/{id}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_200_OK
    assert data['username'] == payload['username']
    assert data['email'] == payload['email']
@pytest.mark.django_db
def test_partial_update_user_without_permission_return_401(getClient):
    cleint1,id1 = getClient()
    cleint2,id2 = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(username="ali",email="ali@gmail.com",bio="LOLyangm")
    response = cleint1.put(f"/user/{id2}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
@pytest.mark.django_db
def test_partial_update_user_without_permission_missing_username_return_401(getClient):
    cleint1,id1 = getClient()
    cleint2,id2 = getClient({"username":"hassan","email":"hassan@gmail.com","password":"123456!_"})
    payload = dict(email="ali@gmail.com",bio="LOLyangm")
    response = cleint1.put(f"/user/{id2}/",payload)
    data = response.data
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
