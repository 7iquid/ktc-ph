from django import forms
from django.forms import ModelForm
from .models import Photo

class NameForm(forms.Form):
    part_name = forms.CharField(label='Part Name', max_length=100)
    part_no = forms.CharField(label='Part No', max_length=100)
    part_image = forms.CharField(label='Your name', max_length=100)

class PhotoForm(ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'