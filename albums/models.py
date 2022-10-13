from django.db import models
from artists.models import Artist
from model_utils.models import TimeStampedModel
# Create your models here.
class Album(TimeStampedModel):
    name = models.CharField(default='New Album',max_length=255)
    release_date =  models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False,decimal_places=2,max_digits=15)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    album_approved = models.BooleanField(default=False)
    def __str__(self):
        return (f"Name:{self.name},Cost:{self.cost}")    


