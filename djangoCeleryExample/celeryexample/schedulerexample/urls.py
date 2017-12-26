from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'home', home, name='home'),
        url(r'tasks', tasks, name='tasks'),
        url(r'periodictask', setup_periodic_tasks, name='periodictasks'),
        ]
