from django.db import models


class Movies(models.Model):
    name=models.CharField(max_length=250)
    desc=models.CharField(max_length=250)
    year=models.IntegerField()
    imag=models.ImageField(upload_to="gallery")

def __str__(self):
    return self.name