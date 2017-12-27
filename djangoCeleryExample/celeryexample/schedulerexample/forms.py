from django import forms
from django.forms import ModelForm, Textarea
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import Field
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, HTML

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

class SchedulePeriodicTaskForm(forms.Form):
    """
    Form class to schedule a periodic task
    """
    name = forms.CharField(label='Name', max_length=128)
    frequency = forms.ChoiceField(label='Frequency', choices=[(5, 'Every 5 Minutes'),
                                                              (10, 'Every 10 Minutes'),
                                                              (20, 'Every 20 Minutes'),
                                                              (60, 'Every Hour'),
                                                              (6, 'Every 6 Hours'),
                                                              (12, 'Every 12 Hours'),
                                                              (24, 'Every Day'),
                                                              (0, 'At a specific time of the day'),])
    time = forms.TimeField(label='Time', required=False, widget=forms.TimeInput(format='%H:%M'))

    def __init__(self, *args, **kwargs):
        super(SchedulePeriodicTaskForm,self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-add-periodic-tassk-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'bootstrap-horizontal'
        self.helper.add_input(Submit('addperiodictask', 'Add Periodic Task', css_class='btn-primary'))

        self.helper.layout = Layout(
                Fieldset('Setup a Periodic Task',
                    Field('name', placeholder='Enter a unique name for your periodic task'),
                    Field('frequency'),
                    Field('time'),
                    HTML("{% load render_table from django_tables2 %}{% render_table table %}")))

    def clean(self):
        cleaned_data = super(SchedulePeriodicTaskForm, self).clean()
        frequency = cleaned_data.get('frequency')
        time = cleaned_data.get('time')
        if int(frequency) == 0 and time == None:
            raise forms.ValidationError(
                    "Time cannot be empty"
                )
