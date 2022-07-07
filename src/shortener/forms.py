from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import UserURL


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = '__all__'


class UserURLForm(forms.ModelForm):

    class Meta:
        model = UserURL
        fields = ['author', 'full_url']
        widgets = {'author': forms.HiddenInput}
