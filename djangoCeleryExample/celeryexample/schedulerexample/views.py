# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from celery.schedules import crontab
from datetime import datetime, timedelta

from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .tasks import test
from .forms import AddTaskForm

# Create your views hereo.

def home(request):
    return render(request, "login_home.html")

@method_decorator(login_required, name='dispatch')
class Addtask(CreateView):
    form_class = AddTaskForm
    template_name = 'schedulerexample/add_task.html'
    success_url = reverse_lazy('listtasks')

def listtasks(request):
    return render(request, "login_home.html")

def addperiodictask(request):
    return render(request, "login_home.html")

def addonetimetask(request):
    return render(request, "login_home.html")

def periodictaskstatus(request):
    return render(request, "login_home.html")

def onetimetaskstatus(request):
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
