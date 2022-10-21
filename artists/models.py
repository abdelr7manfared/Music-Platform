

from django.db import models
# Create your models here.
class Artist(models.Model):
    Stage_name = models.CharField(unique=True,max_length=255,blank=False)
    Social_link_field = models.URLField(null=False,blank=True)
    class Meta:
        ordering = ('Stage_name',)
    def approved_albums(self):
        return self.album_set.filter(album_approved__exact=True).count()
    def __str__(self):
        return (f"StageName:{self.Stage_name} ,SocialLink: {self.Social_link_field} , Albums:{self.album_set.all()}")
    def get_Stagename(self):
        return self.Stage_name

