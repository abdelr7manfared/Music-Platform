from django.contrib import admin
from . import models
#from albums.models import Album
#from albums.admin import AlbumInline
# Register your models here.

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=['Stage_name','Social_link_field','approved_albums']
    #inlines=[AlbumInline]
    def approved_albums(self,artist):
        return artist.approved_albums()    
	