from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    login = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'aria-describedby':"emailHelp",
                                                    'placeholder':"Введите ваш логин..."
                                                    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
                                                    'type':'password',
                                                    'class': 'form-control form-control-user',
                                                    'id':"exampleInputPassword",
                                                    'placeholder':"Введите ваш пароль..."
                                                    }))