from django import forms
from .models import  factmulti


class FactUploadForm(forms.ModelForm):
    class Meta:
        model = factmulti
        fields = ['id','photo']