from ..serializers import AlbumSerializer
import pytest
from django.core import serializers
from ..models import Album
@pytest.mark.django_db
def test_serializer(artist):
    payload = dict(name= "Marwan Pablo",release_date= "2022-10-15T12:04:06Z",cost= "19.00")
    serializer = AlbumSerializer(data=payload)
    assert serializer.is_valid()
    serializer.save(artist=artist)
    assert "id" in serializer.data
    assert serializer.data['name'] == payload['name']
    assert serializer.data['release_date'] == payload['release_date']
    assert serializer.data['cost'] == payload['cost']
    assert "Stage_name" in serializer.data['artist']
    assert "Social_link_field" in serializer.data['artist']
    assert "user" in serializer.data['artist']
    assert serializer.errors == {}
@pytest.mark.django_db
def test_serializer_missing_name(artist):
    payload = dict(release_date= "2022-10-15T12:04:06Z",cost= "19.00")
    serializer = AlbumSerializer(data=payload)
    assert serializer.is_valid()
    serializer.save(artist=artist)
    assert "id" in serializer.data
    assert serializer.data['name'] == 'New Album'
    assert serializer.data['release_date'] == payload['release_date']
    assert serializer.data['cost'] == payload['cost']
    assert "Stage_name" in serializer.data['artist']
    assert "Social_link_field" in serializer.data['artist']
    assert "user" in serializer.data['artist']
    assert serializer.errors == {}

@pytest.mark.django_db
def test_serializer_missing_release_date():
    payload = dict(name= "Marwan Pablo",cost= "19.00")
    serializer = AlbumSerializer(data=payload)
    assert not serializer.is_valid()
    assert 'release_date' in serializer.errors

@pytest.mark.django_db
def test_serializer_missing_cost():
    payload = dict(name= "Marwan Pablo",release_date= "2022-10-15T12:04:06Z")
    serializer = AlbumSerializer(data=payload)
    assert not serializer.is_valid()
    assert 'cost' in serializer.errors