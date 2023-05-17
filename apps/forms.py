from django import forms
from apps.models import Document


class DocForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
