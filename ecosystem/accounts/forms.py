from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class LoginForm(forms.Form):
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

class RegistrationForm(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"Имя"
                                                    }), 
                                                    required=True)
    
    middle_name = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"Отчество"
                                                    }))
    
    last_name = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"Фамилия"
                                                    }), required=True)
    date_of_birth = forms.DateTimeField(input_formats=['%d.%m.%Y'], widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"ДД/ММ/ГГ"
                                                    }),required=True)
    
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"89999999999"
                                                    }), required=True)
    
    email = forms.EmailField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"test@miet.ru"
                                                    }),required=False)
    
    login = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control form-control-user',
                                                    'placeholder':"Логин для входа"
                                                    }), required=True)
    
    password = forms.CharField(label='Password', widget=forms.TextInput(attrs={
                                                    'type':'password',
                                                    'class': 'form-control form-control-user',
                                                    'id':"exampleInputPassword",
                                                    'placeholder':"Пароль для входа"
                                                    }), required=True)
    
    