from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class AssignmentForm(ModelForm):
    class Meta:
        model = Assignment
        fields = '__all__'


class SubmitAssignment(ModelForm):
    class Meta:
        model = Answer
        fields = ['staffname', 'assignmentname', 'regno', 'answer']
