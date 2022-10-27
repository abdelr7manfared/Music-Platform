import pytest
from rest_framework.test import APIClient
from artists.models import Artist
@pytest.fixture
def api_client():
    Artist.objects.create(Stage_name="artist1",Social_link_field= "https://www.instagram.com/artist1/")
    Artist.objects.create(Stage_name="artist2",Social_link_field= "https://www.instagram.com/artist2/")
    return APIClient()
