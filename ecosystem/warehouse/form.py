
from unicodedata import name
from django import forms
from warehouse.models import Warehouse

# product = Warehouse.objects.all()
# print(product)

class Order(forms.Form):
    product_name = forms.CharField(widget=forms.TextInput(attrs={
                                                    'class': 'form-control',
                                                    'placeholder': "product"
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
                                    

