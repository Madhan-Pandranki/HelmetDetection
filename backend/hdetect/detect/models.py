from django.db import models

class Frame(models.Model):
    video = models.FileField(null=True ,upload_to='videos/')

class MyModel(models.Model):
    image = models.FileField()
