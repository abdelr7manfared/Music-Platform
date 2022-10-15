from django.contrib import admin
from . import models

@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display=['Stage_name','Social_link_field','approved_albums']
    def approved_albums(self,artist):
        return artist.approved_albums()    
	