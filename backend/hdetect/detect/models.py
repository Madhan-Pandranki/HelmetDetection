from django.db import models

class Frame(models.Model):
    file=models.FileField(null=True,blank=True)

# class MyModel(models.Model):
    # image = models.FileField()

class NameURL(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()


    # video = models.FileField(upload_to='videos/', null=True, blank=True)
    # image = models.ImageField(upload_to='images/', null=True, blank=True)