from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.name + " at " + str(self.url)

class Book(models.Model):
    title = models.CharField(max_length=200)
    numpages = models.IntegerField()

    publisher = models.ForeignKey(Publisher,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True
                                     )

    def __str__(self):
        return self.title + " pp. " + str(self.numpages)

class Author(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    books = models.ManyToManyField(Book)

    class Meta:
        ordering = ['firstname', 'lastname']

    def __str__(self):
        return self.firstname + " " + self.lastname
