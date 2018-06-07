from django.db import models

from timeline.models import Timeline

# Create your models here.

class Comments(models.Model):
        id = models.AutoField(primary_key=True)
        name = models.CharField(max_length=100)
        comment = models.TextField()
        timeline = models.ForeignKey(Timeline,on_delete = models.CASCADE)

