from django.db import models
from django.utils import timezone
from artists.models import Artist
# Create your models here.
class Album(models.Model):
    name = models.CharField(default='New Album',max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    release_date =  models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False,decimal_places=2,max_digits=15)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    def __str__(self):
        return (f"Name:{self.name},CreationDate:{self.creation_date},ReleaseDate:{self.release_date},Cost:{self.cost}")


    
