from django.contrib import admin
from . import models
from artists.models import Artist
from .form import AlbumForm
# Register your models here.
class AlbumInline(admin.StackedInline):
    model= models.Album
    extra= 0


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    list_display=['name','created','release_date','cost','artist','album_approved',]
    readonly_fields=['created']
