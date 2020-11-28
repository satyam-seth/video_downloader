from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='youtube_index'),
    path('<int:id>/<int:itag>/',views.download,name='youtube_downloads'),
]