from django.db import models

class Frame(models.Model):
    video = models.FileField(null=True)
    frame_number = models.IntegerField(null=True)
    image = models.FileField(null=True)
