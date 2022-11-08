from django import forms
from .models import Gallery

# class GalleryUploadForm(forms.Form):
#     class Meta:
#         model = Gallery
#         fields = '__all__'





class GalleryUploadForm(forms.Form):
    image = forms.FileField()
