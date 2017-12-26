from django.conf.urls import url
from .views import *

urlpatterns = [
        url(r'^home$', home, name='home'),
        url(r'^tasks$', tasks, name='tasks'),
        url(r'^periodictask$', setup_periodic_tasks, name='periodictasks'),
        ]

"""
Urls for task
"""

urlpatterns += [
        url(r'^addtask$', Addtask.as_view(), name='addtask'),
        url(r'^updatetask/(?P<pk>\d+)/$', Updatetask.as_view(), name='updatetask'),
        url(r'^deletetask/(?P<pk>\d+)/$', Deletetask.as_view(), name='deletetask'),
        url(r'^listtasks$', listtasks, name='listtasks'),
        ]
"""
urls for scheduling
"""

urlpatterns += [
        url(r'^addperiodictask$', addperiodictask, name='addperiodictask'),
        url(r'^addonetimetask$', addonetimetask, name='addonetimetask'),
        ]

"""
urls for monitoring
"""

urlpatterns += [
        url(r'^periodictaskstatus$', periodictaskstatus, name='periodictaskstatus'),
        url(r'^onetimetaskstatus$', onetimetaskstatus, name='onetimetaskstatus'),
        ]
