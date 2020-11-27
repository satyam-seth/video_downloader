from django.urls import path
from . import views

urlpatterns = [
    path('go/',views.go,name='youtube_go'),
]