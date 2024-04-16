from django import forms
from .models import Frame,MyModel,NameURL

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Frame
        fields = ['video']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model =MyModel
        fields =['image']

class NameURLForm(forms.ModelForm):
    class Meta:
        model = NameURL
        fields = ['name', 'url']