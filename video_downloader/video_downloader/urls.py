from django.contrib import admin
from django.urls import path,include
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('youtube/', include('youtube_downloader.urls')),
    path('facebook/', include('facebook_downloader.urls'))
]