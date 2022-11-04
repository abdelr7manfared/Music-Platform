
from celery import shared_task
from artists.models import Artist
from users.models import User
from django.core.mail import send_mail
from django.conf import settings
from time import sleep
from datetime import datetime, timedelta
@shared_task()
def Congratulation_mail(artist_id):
    artist = Artist.objects.get(pk=artist_id)
    artist_email = artist.user.email
    print(artist_email)
    send_mail("Created successfully",'Congratulations ',settings.EMAIL_HOST_USER
    ,[artist_email])

@shared_task(name="notify_user")
def notify_user():
    try:
        time = datetime.now().date()  - timedelta(days=30)
        allartist = Artist.objects.all()
        for artist in allartist:
            artist = Artist.objects.get(pk=artist.id)
            artist_email = artist.user.email
            print(artist.user.username)
            last_published  = artist.album_set.all().order_by('-created').first().created.date()
            print(last_published,time)
            if last_published < time:
                send_mail("Warning",'inactivity is causing their popularity on our platform to decrease ',settings.EMAIL_HOST_USER,[artist_email])
        return 'Success'
    except Exception as error:
        return 'Fail'


