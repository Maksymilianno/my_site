from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    biography = models.TextField()


class Book(models.Model):
    title = models.CharField(max_length=128)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=64)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.title


class Reviewer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
