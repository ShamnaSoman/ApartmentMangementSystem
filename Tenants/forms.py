from django.forms import ModelForm, widgets, forms
from django import forms
from .models import Tenants


class tenantform(forms.ModelForm):
    Email = forms.EmailField(disabled=True)

    class Meta:
        model = Tenants
        fields = '__all__'
        widgets={
            'Name' : forms.TextInput(attrs={'calss':'form-control'}),
            'Mobile': forms.NumberInput(attrs={'calss': 'form-control'})
        }



