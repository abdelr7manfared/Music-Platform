from django.db import models
from django.core.validators import FileExtensionValidator
from artists.models import Artist
from model_utils.models import TimeStampedModel
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from .task import Congratulation_mail
from django.db.models.signals import post_save
from django.utils.html import mark_safe
# Create your models here.
class Album(TimeStampedModel):
    name = models.CharField(default='New Album',max_length=255)
    release_date =  models.DateTimeField(blank=False)
    cost = models.DecimalField(blank=False,decimal_places=2,max_digits=15)
    artist = models.ForeignKey(Artist,on_delete=models.CASCADE)
    album_approved = models.BooleanField(default=False)
    def __str__(self):
        return (f"Name:{self.name},Cost:{self.cost},Song:{self.song_set.all()}")    

def send_email(sender, instance,**kwargs):
    Congratulation_mail.delay(instance.artist.id)

post_save.connect(send_email, sender=Album)
    

class Song(models.Model):
    name = models.CharField(max_length=255,blank=True)
    image = models.ImageField(upload_to="images/",blank=False)
    image_thumbnail = ImageSpecField(source='image',format="JPEG",processors=[ResizeToFill(100, 50)],)
    audio = models.FileField(upload_to="musics/",blank=False,validators=[FileExtensionValidator(allowed_extensions=['mp3','wav'])])
    album = models.ForeignKey(Album,on_delete=models.CASCADE)
    def save(self,*args, **kwargs):
        if self.name == "":
            self.name = self.album.name
        super().save(*args, **kwargs)
    def __str__(self):
        return (f"name : {self.name} ,Album_id :{self.album_id}")
    def image_tag(self):
            return mark_safe('<img src="%s" height=200px;  width=200px/>' % self.image.url)
    def music_tag(self):
        return mark_safe('<audio controls><source src="%s" ></audio>'%self.audio.url)
    def image_thumbnail_tag(self):
            return mark_safe('<img src="%s" />' % self.image_thumbnail.url)


