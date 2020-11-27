from django.shortcuts import render

# Create your views here.

def go(request):
    context={
        'youtube_active':'active',
        'youtube_disabled':'disabled',
        }
    return render(request,'youtube_downloader/youtube.html',context)