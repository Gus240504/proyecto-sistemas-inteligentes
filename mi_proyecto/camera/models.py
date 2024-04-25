from django.db import models

class CameraStream(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
# Create your models here.
class Meta:
        app_label = 'camera'