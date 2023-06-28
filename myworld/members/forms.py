from django import forms
from .models import MyData

class MyDataForm(forms.ModelForm):
    class Meta:
        model = MyData
        fields = ['field1', 'field2']