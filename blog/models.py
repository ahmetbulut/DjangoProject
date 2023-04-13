from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField()

class Book(models.Model):
    title = models.CharField(max_length=100)
    numpages = models.IntegerField()
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + " pp. " + str(self.numpages)