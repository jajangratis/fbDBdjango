from django.db import models

# Create your models here.

class Timeline(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    status = models.TextField()
    like = models.IntegerField(default=0)
    pic = models.CharField(max_length=100,null=True)
