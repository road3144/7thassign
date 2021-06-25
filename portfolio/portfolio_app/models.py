from django.db import models

# Create your models here.
class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='images/',default='')

    def __str__(self):
        return self.titleß