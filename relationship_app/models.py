from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Book(models.Model):
    title = models.CharField(max_length=32)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

class Library(models.Model):
    name = models.CharField(max_length=255)
    book = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=250)
    library = models.OneToOneField(Library, on_delete=models.CASCADE)

