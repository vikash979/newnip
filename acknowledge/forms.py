from django import forms
from django.forms import ClearableFileInput 
from .models import UploadPdf

class ResumeUpload(forms.ModelForm):
    class Meta:
        model = UploadPdf
        fields = ['resumes']
        widgets = {
            'resumes': ClearableFileInput(attrs={'multiple': True}),
        }