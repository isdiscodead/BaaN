from django import forms
from django.forms import ModelForm
from todoapp.models import Todo


class TodoCreationForm(ModelForm):
    class Meta:
        model = Todo
        fields = ['content']

    content = forms.CharField(
        label="",
        widget=forms.TextInput(attrs={
            "placeholder": "enter your task",
            "class": "account_form_input",
            "style": "margin-bottom: 0rem;"
        })
    )
