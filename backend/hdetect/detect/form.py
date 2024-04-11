from django import forms
from .models import Frame

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ['video']
