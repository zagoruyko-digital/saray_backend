from django.db import models
from django.conf import settings

class Manager(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.FileField(upload_to='./public_img')