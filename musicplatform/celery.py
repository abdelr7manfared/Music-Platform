
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "musicplatform.settings")
app = Celery("musicplatform")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.beat_schedule ={
      'notify_user': {
        'task': 'notify_user',
        'schedule': crontab(minute='*/24'),
    },
}