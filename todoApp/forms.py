from django import forms
from .models import MyTodo


class TodoForm(forms.ModelForm):
    class Meta:
        model = MyTodo
        fields = ['task']
