from django.shortcuts import render,redirect
from .models import FacebookRecord
from .forms import FacebookDownloadForm
from django.contrib import messages
import requests as r
import re

# Create your views here.

def index(request):    
    if request.method=='POST':
        fm=FacebookDownloadForm(request.POST)
        if fm.is_valid():
            link=fm.cleaned_data['link']
            pst=FacebookRecord(link=link)
            pst.save()
        fm=FacebookDownloadForm()
        try:
            html = r.get(link)
            sdvideo_url=re.search('sd_src:"(.+?)"', html.text)[1]
            hdvideo_url = re.search('hd_src:"(.+?)"', html.text)[1]
        except:
            messages.warning(request,'Sorry something went wrong !!')
            return redirect('facebook_index')
        context={
            'facebook_active':'active',
            'facebook_disabled':'disabled',
            'form':fm,
            'download':True,
            'sdvideo_url':sdvideo_url,
            'hdvideo_url':hdvideo_url,
            }
    else:
        fm=FacebookDownloadForm()
        context={
            'facebook_active':'active',
            'facebook_disabled':'disabled',
            'form':fm
            }
    return render(request,'facebook_downloader/facebook.html',context)
