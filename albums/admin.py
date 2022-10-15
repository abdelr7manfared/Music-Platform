from django.contrib import admin
from . import models
from .models import Album
from django.core.exceptions import ValidationError
from .form import AlbumForm, SongForm

# Register your models here.
class AlbumInline(admin.StackedInline):
    model= models.Album
    extra= 0

class SongInline(admin.StackedInline):
    model= models.Song
    extra= 0
    min_num = 1

@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    inlines=[SongInline]
    list_display=['name','created','release_date','cost','artist','album_approved',]
    readonly_fields=['created']



@admin.register(models.Song)
class SongAdmin(admin.ModelAdmin):
    form=SongForm
    list_display= ['name','image_tag','image_thumbnail_tag','music_tag']
    class Meta:
        model = models.Song

    def delete_queryset(self, request, queryset):
        LastOne = 0
        for i in queryset:
            if len(Album.objects.filter(pk=i.album_id).values('song')) == 1:
                LastOne = 1
        if LastOne:
            raise ValidationError("Must Exist at least one song in each album")
        else : queryset.delete()


    def delete_model(self, request, obj):
        if len(Album.objects.filter(pk=obj.album_id).values('song')) > 1:
            obj.delete()
        else :
            raise ValidationError("Must Exist at least one song in each album")
    
