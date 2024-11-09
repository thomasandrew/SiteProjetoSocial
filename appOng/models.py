from django.db import models

# Create your models here.
class Gallery(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title    
    
class Gallery_home(models.Model):
    title = models.CharField(max_length=70)
    image = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.title        