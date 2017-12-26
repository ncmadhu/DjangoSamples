from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set the default django settings module for the celery program
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celeryexample.settings')

app = Celery('celeryexample')

# namespace="CELERY' means all configurations related to celery
# starts with prefix CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs
app.autodiscover_tasks()
