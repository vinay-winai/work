from django.db import models

class Userlog(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100,default="missing")
    ip = models.CharField(max_length=45,default="missing")
    timestamp = models.CharField(max_length=50,default="missing")