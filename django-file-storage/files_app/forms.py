from django import forms
from .models import UploadedFile

# Form for uploading files
class UploadFileForm(forms.ModelForm):

    class Meta:
        model = UploadedFile
        fields = ['title', 'file']