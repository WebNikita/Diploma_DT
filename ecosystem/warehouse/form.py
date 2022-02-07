
from django import forms

class Order(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder':"Имя пользователя"
                                                    }), 
                                                    required=True,
                                                    disabled=True)
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder':"Количество"
                                                    }), 
                                                    required=True)
    message_text = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder':"Для чего"
                                                    }), 
                                                    required=True)
                                    

