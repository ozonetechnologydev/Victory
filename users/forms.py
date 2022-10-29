from django import forms
from dataclasses import field
from django.contrib.auth.models import Group




class UserGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control","required":True, "placeholder":"Name",}),
            'permissions': forms.SelectMultiple(attrs={"required":True,'class': 'multi-select'}),
        }