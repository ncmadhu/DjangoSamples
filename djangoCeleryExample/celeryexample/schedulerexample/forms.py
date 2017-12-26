from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset

from .models import CeleryTask

class TaskForm(ModelForm):
    """
    Base class for TaskForm
    """
    class Meta:
        model = CeleryTask
        fields = ['task_name', 'task_description', 'task_args']
        labels = {'task_name': _('Task Name'),
                'task_description': _('Task Description'),
                'task_args':_('Task Arguements'),}
        widgets = {
            'task_description': Textarea(attrs={'cols': 50, 'rows': 10}),
            'task_args': Textarea(attrs={'cols': 50, 'rows': 3}),
        }

class AddTaskForm(TaskForm):
    """
    Form class to Add a task to DB
    """

    def __init__(self, *args, **kwargs):
        super(AddTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-add-task-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'bootstrap-horizontal'
        self.helper.add_input(Submit('submit', 'Add Task', css_class='btn-primary'))

        self.helper.layout = Layout(
                Fieldset('Add task',
                    Field('task_name', placeholder='Enter the name of the task'),
                    Field('task_description', placeholder='Enter the description of the task'),
                    Field('task_args', widget=forms.Textarea(), rows=3, placeholder='Enter the arguements for the task as a list item'),))

class UpdateTaskForm(TaskForm):
    """
    Form class to Add a task to DB
    """

    def __init__(self, *args, **kwargs):
        super(UpdateTaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-update-task-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'bootstrap-horizontal'
        self.helper.add_input(Submit('update', 'Update', css_class='btn-primary'))
        self.helper.add_input(Submit('delete', 'Delete', css_class='btn-danger'))

        self.helper.layout = Layout(
                Fieldset('Update/Delete task',
                    Field('task_name', placeholder='Enter the name of the task'),
                    Field('task_description', placeholder='Enter the description of the task'),
                    Field('task_args', widget=forms.Textarea(), rows=3, placeholder='Enter the arguements for the task as a list item'),))
