# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from celery.schedules import crontab
from datetime import datetime, timedelta

from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django_tables2 import RequestConfig
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .tasks import test
from .models import CeleryTask
from .tables import CeleryTaskTable
from .forms import AddTaskForm, UpdateTaskForm, SchedulePeriodicTaskForm

# Create your views hereo.

def home(request):
    return render(request, "login_home.html")

@method_decorator(login_required, name='dispatch')
class Addtask(CreateView):
    form_class = AddTaskForm
    template_name = 'schedulerexample/add_task.html'
    success_url = reverse_lazy('listtasks')

@method_decorator(login_required, name='dispatch')
class Updatetask(UpdateView):
    model =  CeleryTask
    form_class = UpdateTaskForm
    template_name = 'schedulerexample/add_task.html'
    success_url = reverse_lazy('listtasks')

    def post(self, request, *args, **kwargs):
        print request.POST
        if 'delete' in request.POST:
            self.object = self.get_object()
            return HttpResponseRedirect(reverse('deletetask', kwargs={'pk': self.object.pk}))
        else:
            return super(Updatetask, self).post(request, *args, **kwargs)

@method_decorator(login_required, name='dispatch')
class Deletetask(DeleteView):
    model =  CeleryTask
    template_name = 'schedulerexample/delete_task.html'
    success_url = reverse_lazy('listtasks')

@login_required
def listtasks(request):
    table = CeleryTaskTable(CeleryTask.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'schedulerexample/list_task.html', {'table': table})

@login_required
def addperiodictask(request):
    if request.method == 'POST':
        form = SchedulePeriodicTaskForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect(reverse('listtasks'))
    else:
        form = SchedulePeriodicTaskForm
    table = CeleryTaskTable(CeleryTask.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'schedulerexample/add_periodic_task.html', {'form' : form, 'table': table})

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
