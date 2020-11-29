from django.shortcuts import redirect, render
from .models import YoutubeRecord
from .forms import YoutubeDownloadForm
from pytube import YouTube
from django.http import FileResponse

# Create your views here.

def index(request):
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
        try:
            yt=YouTube(link)
        except:
            return redirect('home') # sorry.html
        tumbnail_url=yt.thumbnail_url
        title=yt.title
        length=yt.length
        desc=yt.description
        view=yt.views
        videos=yt.streams.filter(progressive=True)
        context['embed_link']=link.replace('watch?v=','embed/')
        context['tumbnail_url']=tumbnail_url
        context['view']=view
        context['length']=length
        context['desc']=desc
        context['download']=True
        context['title']=title
        context['videos']=videos
        context['id']=pst.id
    else:
        fm=YoutubeDownloadForm()
    context['form']=fm
    return render(request,'youtube_downloader/youtube.html',context)

def download(request,id,itag):
    req=YoutubeRecord.objects.get(pk=id)
    yt=YouTube(req.link)
    stream=yt.streams.get_by_itag(itag)
    data=stream.download(skip_existing=True)
    return FileResponse(open(data,'rb'))