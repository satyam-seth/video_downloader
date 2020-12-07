from django.contrib import admin
from .models import FacebookRecord

# Register your models here.

@admin.register(FacebookRecord)
class FacebookRecordAdmin(admin.ModelAdmin):
    list_display=('id','link','date_time')