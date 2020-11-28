from django.contrib import admin
from .models import YoutubeRecord

# Register your models here.

@admin.register(YoutubeRecord)
class YoutubeRecordAdmin(admin.ModelAdmin):
    list_display=('id','link','date_time')