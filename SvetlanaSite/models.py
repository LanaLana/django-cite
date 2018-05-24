from django.db import models
from django.utils import timezone


class Book(models.Model):
    author = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.CharField(max_length=200)
    published_date = models.DateTimeField()


    def __str__(self):
        return self.title + "."


class Video(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    url = models.CharField(max_length=200)

    def __str__(self):
        return self.title + "."


class Picture(models.Model):
    title = models.CharField(max_length=200, default='cfjdnjv')
    img1 = models.ImageField(blank=True)
    img2 = models.ImageField(blank=True)
    year = models.IntegerField(default=2017)

    def __str__(self):
        return self.title + "."


class Journal(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title + "."
