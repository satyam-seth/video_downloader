from django.urls import path
from . import views

urlpatterns = [
    path('go/',views.youtube_go,name='youtube_go'),
    path('downloads/',views.youtube_downloads,name='downloads'),
]