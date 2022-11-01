import pytest
from rest_framework import status
@pytest.mark.django_db
def test_logout_user_return_204(auth_client):
    response = auth_client.post('/authentication/logout/')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_logout_user_unauthenticated_return_401(client):
    response = client.post('/authentication/logout/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
