import pytest
from rest_framework.test import APIClient
from artists.models import Artist
@pytest.fixture()
def artist():
    artist =  Artist.objects.create(Stage_name="artist1",Social_link_field= "https://www.instagram.com/artist1/")
    return artist
@pytest.fixture
def client():
    return APIClient()
