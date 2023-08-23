from django.db import models


# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    publication_year = models.PositiveIntegerField()
    isbn = models.CharField(max_length=13, unique=True)
    genre = models.CharField(max_length=64)


class Reviewer(models.Model):
    login = models.CharField(max_length=32, unique=True)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)
    join_date = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.PositiveIntegerField()
    publication_date = models.DateTimeField(auto_now_add=True)


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    content = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)


class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birth_date = models.DateField()
    biography = models.TextField()
