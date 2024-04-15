from django import forms
from .models import Frame,MyModel

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ['video']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model =MyModel
        fields =['image']
