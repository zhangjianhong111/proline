from django.db import models




class Gallery(models.Model):
    objects = None
    description=models.CharField(max_length=100)



