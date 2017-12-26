# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from datetime import datetime, timedelta
from celery.schedules import crontab

from django.shortcuts import render
from django_celery_beat.models import PeriodicTask, IntervalSchedule

from .tasks import test

# Create your views hereo.

def home(request):
    return render(request, "login_home.html")

def tasks(request):
    return render(request, "home.html", {"status": "working ... but pending"})

def setup_periodic_tasks(request):
    schedule, created = IntervalSchedule.objects.get_or_create(
            every=10,
            period=IntervalSchedule.SECONDS,
            )
    PeriodicTask.objects.create(
            interval=schedule,
            name='Sample tasks',
            task='schedulerexample.tasks.test',
            args=json.dumps(['arg1']),
            expires=datetime.utcnow() + timedelta(seconds=30)
            )
    return render(request, "home.html", {"status": "periodic task scheduled"})
