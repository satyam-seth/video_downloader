from django.shortcuts import render
from .models import YoutubeRecord
from .forms import YoutubeDownloadForm

# Create your views here.

def youtube_go(request):
    context={
            'youtube_active':'active',
            'youtube_disabled':'disabled',
            }
    if request.method=='POST':
        fm=YoutubeDownloadForm(request.POST)
        if fm.is_valid():
            link=fm.cleaned_data['link']
            pst=YoutubeRecord(link=link)
            pst.save()
        fm=YoutubeDownloadForm()
        context['embed_link']=link.replace('watch?v=','embed/')
        print(context['embed_link'])
        context['download']=True
    else:
        fm=YoutubeDownloadForm()
    context['form']=fm
    print(context)
    return render(request,'youtube_downloader/youtube.html',context)

def youtube_downloads(request):
    context={
        'youtube_active':'active',
        'youtube_disabled':'disabled',
        }
    return render(request,'youtube_downloader/youtube.html',context)