from django.db import models

# Create your models here.
class IceCream(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    weight = models.IntegerField(("Weight"))
    category = models.CharField(("Category"), max_length=50)
    image = models.ImageField(upload_to='ice_creams/')

    def __str__(self):
        return self.name