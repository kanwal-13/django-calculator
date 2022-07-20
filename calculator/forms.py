from typing_extensions import Required
from django import forms

class FormName(forms.Form):
         # each field would be mapped as an input field in HTML
        num1 = forms.IntegerField(required = False)
        num2 = forms.IntegerField(required = False)