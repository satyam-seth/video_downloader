from django import forms
from .models import FacebookRecord

class FacebookDownloadForm(forms.ModelForm):
    class Meta:
        model=FacebookRecord
        fields=('link',)
        widgets={
            'link':forms.URLInput(attrs={'class':'form-control shadow-lg','placeholder':'paste your video link here'})
        }