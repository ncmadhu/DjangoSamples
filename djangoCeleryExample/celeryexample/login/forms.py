import re

from django import forms
from django.core.urlresolvers import reverse
#from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

from crispy_forms.bootstrap import Field, TabHolder, Tab
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, Fieldset

from .models import User

username_regex = re.compile('^[\w.@ +-]+$',re.UNICODE)

class RegistrationForm(forms.Form):
    """
    Form to handle user registration
    """

    first_name =  forms.CharField(required=True, max_length=255)
    last_name = forms.CharField(required=True, max_length=255)
    email = forms.EmailField(required=True)
    username = forms.RegexField(regex=username_regex, widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Confirm Password"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("username already exists please try another username"))

    def clean(self):
        if 'password' in self.cleaned_data and 'confirm_password' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['confirm_password']:
                raise forms.ValidationError(_("Password and Confirm Password doesnt match"))
        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        """
        Initialize form
        """
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-registration-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'bootstrap-horizontal'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-success'))
        self.helper.layout = Layout(
                Fieldset('User Details',
                    Field('first_name', placeholder='Your first name'),
                    Field('last_name', placeholder='Your last name'),
                    Field('username', placeholder='Choose a user name'),
                    Field('email', placeholder='Your email id'),
                    Field('password', placeholder='Enter password'),
                    Field('confirm_password', placeholder='Type password again'),),)


class LoginForm(forms.Form):
    """
    Form to handle user login
    """
    username = forms.RegexField(regex=username_regex, widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    password = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=30, render_value=False)), label=_("Password"))

    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            raise forms.ValidationError(_("username doesnt exist"))
        return self.cleaned_data['username']

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError(_('username and password doesnt match'))
        return self.cleaned_data

    def login(self, request):
        """
        Authenticate the user
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

    def __init__(self, *args, **kwargs):
        """
        Initialize form
        """
        super(LoginForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-login-data-form'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.form_class = 'bootstrap-horizontal'
        self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))
        self.helper.layout = Layout(
                Fieldset('User Details',
                    Field('username', placeholder='Choose a user name'),
                    Field('password', placeholder='Enter password'),),)
