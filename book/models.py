from django.db import models
from user.models import User


class Genre(models.Model):
    genre = models.CharField(max_length=50, unique=True, verbose_name='genre')

    def __str__(self):
        return self.genre

    class Meta:
        verbose_name_plural = "genres"


class Condition(models.Model):
    condition = models.CharField(max_length=50, unique=True, verbose_name='condition')

    def __str__(self):
        return self.condition


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    b_day = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='author_images', null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.b_day.year}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(default="No description")
    pages = models.IntegerField(null=True, blank=True)
    author = models.ManyToManyField(Author, verbose_name='author')
    genre = models.ManyToManyField(Genre, verbose_name='genre')
    condition = models.ManyToManyField(Condition, verbose_name='condition')
    image = models.ImageField(upload_to='book_images', null=True, blank=True)
    is_available = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='owner' )



    def __str__(self):
        return f"{self.title} - {self.owner}"