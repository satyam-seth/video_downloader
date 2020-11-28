from django import forms
from django.forms import fields
from django.forms import widgets
from .models import YoutubeRecord

class YoutubeDownloadForm(forms.ModelForm):
    class Meta:
        model=YoutubeRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }