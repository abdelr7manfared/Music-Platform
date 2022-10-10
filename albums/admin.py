from django.contrib import admin
from . import models
from artists.models import Artist
from django.forms import ModelForm

# Register your models here.
class AlbumInline(admin.StackedInline):
    model= models.Album
    extra= 0

class AlbumForm(ModelForm):
    class Meta:
        help_texts={
        'album_approved':'Approve the album if its name is not explicit'
    }

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    list_display=['name','creation_date','release_date','cost','artist','album_approved',]
    readonly_fields=['creation_date']
