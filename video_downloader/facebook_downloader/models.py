from django.db import models

# Create your models here.

class FacebookRecord(models.Model):
    link=models.URLField()
    date_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.link