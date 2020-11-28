from django.db import models

# Create your models here.

class YoutubeRecord(models.Model):
    link=models.URLField()
    date_time=models.DateTimeField(auto_now_add=True)