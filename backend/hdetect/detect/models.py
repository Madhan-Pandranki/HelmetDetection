from django.db import models

class Frame(models.Model):
    video = models.FileField(null=True ,upload_to='videos/')
    # frame_number = models.IntegerField(null=True)
    # image = models.FileField(null=True)

class MyModel(models.Model):
    image = models.FileField()
