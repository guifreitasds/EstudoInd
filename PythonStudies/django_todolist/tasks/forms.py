from django.forms import ModelForm
from django import forms

from .models import *

class TaskForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': "Adicione uma nova tarefa..."}))
    class Meta:
        model = Task
        fields = '__all__'