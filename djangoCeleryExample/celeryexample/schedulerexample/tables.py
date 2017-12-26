import django_tables2 as tables
from django_tables2.utils import A

from .models import CeleryTask

class CeleryTaskTable(tables.Table):
    """
    Table to render list of celery tasks
    """
    update_delete = tables.LinkColumn('updatetask', args=[A('pk')], text='update/delete',orderable=False,empty_values=())
    class Meta:
        model=CeleryTask
        template='django_tables2/bootstrap.html'
        sequence = ('id', 'task_name', 'task_description', 'task_args')
