from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class AccountCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "enter your id",
            "class": "account_form_input",
        })
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "enter your password",
            "class": "account_form_input",
        })
    )

    password2 = forms.CharField(
        label="Password Confirm",
        widget=forms.PasswordInput(attrs={
            "placeholder": "confirm password",
            "class": "account_form_input",
        })
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', ]


class AccountLoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "placeholder": "enter your id",
            "class": "account_form_input",
        })
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            "placeholder": "enter your password",
            "class": "account_form_input",
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        super(AccountLoginForm, self).__init__(*args, **kwargs)  # 꼭 있어야 한다!