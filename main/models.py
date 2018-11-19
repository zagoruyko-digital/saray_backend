from django.db import models
from django.conf import settings

class Manager(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.FileField(upload_to='./public_img')

class News(models.Model):
    manager = models.ForeignKey('Manager', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    cover = models.FileField(upload_to='./public_img')