from django.conf.urls import url, include
from .views import user_registration, user_login, user_logout

urlpatterns = [
        url(r'^register/$', user_registration, name='register'),
        url(r'^login/$', user_login, name='login'),
        url(r'^logout/$', user_logout, name='logout'),
        ]
