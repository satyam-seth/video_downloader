from io import BytesIO
from django.shortcuts import redirect, render
from .models import YoutubeRecord
from .forms import YoutubeDownloadForm
from pytube import YouTube
from django.http import FileResponse
from django.contrib import messages
import os

# Create your views here.

def index(request):
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
            messages.warning(request,'Sorry something went wrong !!')
            return redirect('youtube_index')
        if 'watch?v=' in link:
            embed_link=link.replace('watch?v=','embed/')
        elif 'youtu.be/' in link:
            embed_link=link.replace('youtu.be/','youtube.com/embed/')
        context={
            'youtube_active':'active',
            'youtube_disabled':'disabled',
            'form':fm,
            'embed_link':embed_link,
            'tumbnail_url':yt.thumbnail_url,
            'view':yt.views,
            'desc':yt.description,
            'length':yt.length,
            'title':yt.title,
            'download':True,
            'videos':yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution'),
            'audios':yt.streams.filter(only_audio=True,file_extension='mp4'),
            'id':pst.id
            }
    else:
        fm=YoutubeDownloadForm()
        context={
            'youtube_active':'active',
            'youtube_disabled':'disabled',
            'form':fm
            }
    return render(request,'youtube_downloader/youtube.html',context)

def download(request,id,itag):
    req=YoutubeRecord.objects.get(pk=id)
    yt=YouTube(req.link)
    title=yt.title
    stream=yt.streams.get_by_itag(itag)
    data=stream.download(skip_existing=True)
    path=os.path.normpath(data)
    with open(path,'rb') as f:
        byteData=f.read()
    os.remove(data)
    return FileResponse(BytesIO(byteData),filename=title+'.mp4',as_attachment=True,content_type='application/video/mp4')