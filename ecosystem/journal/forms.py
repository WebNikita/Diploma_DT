from django import forms

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