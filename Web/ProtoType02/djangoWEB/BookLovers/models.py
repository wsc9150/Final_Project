from django.db import models

# Create your models here.


class HealingBook(models.Model) :
    id = models.IntegerField(primary_key=True)
    title = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    keyword = models.TextField(default="")
    image = models.TextField(default="")
    review = models.TextField(default="")
    positive_score = models.FloatField(default=0)
    negative_score = models.FloatField(default=0)

    def __str__(self):
        return self.title


class LibraryBook(models.Model) :
    no = models.IntegerField(primary_key=True)
    bookname = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    publication_year = models.TextField(default="")
    isbn13 = models.TextField(default="")
    addition_symbol = models.TextField(default="")
    vol = models.TextField(default="")
    class_no = models.TextField(default="")
    loan_count = models.IntegerField(default=0)
    bookImageUrl = models.TextField(default="")
    text_reviews_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    num_pages = models.TextField(default="")
    Ratings_Dist = models.TextField(default="")

    def __str__(self):
        return self.no


class AdultBook(models.Model) :
    no = models.IntegerField(primary_key=True)
    bookname = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    publication_year = models.TextField(default="")
    isbn13 = models.TextField(default="")
    addition_symbol = models.TextField(default="")
    vol = models.TextField(default="")
    class_no = models.TextField(default="")
    loan_count = models.IntegerField(default=0)
    bookImageURL = models.TextField(default="")
    text_reviews_count = models.IntegerField(default=0)
    average_rating = models.FloatField(default=0)
    num_pages = models.TextField(default="")
    intro = models.TextField(default="")

    def __str__(self):
        return self.no


class ChildBook(models.Model) :
    no = models.IntegerField(primary_key=True)
    bookname = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    publication_year = models.TextField(default="")
    isbn13 = models.TextField(default="")
    addition_symbol = models.TextField(default="")
    vol = models.TextField(default="")
    class_no = models.TextField(default="")
    loan_count = models.TextField(default="")
    bookImageURL = models.TextField(default="")
    text_reviews_count = models.TextField(default="")
    average_rating = models.TextField(default="")
    num_pages = models.TextField(default="")
    intro = models.TextField(default="")

    def __str__(self):
        return self.no


class TeenagerBook(models.Model) :
    no = models.IntegerField(primary_key=True)
    bookname = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    publication_year = models.TextField(default="")
    isbn13 = models.TextField(default="")
    addition_symbol = models.TextField(default="")
    vol = models.TextField(default="")
    class_no = models.TextField(default="")
    loan_count = models.TextField(default="")
    bookImageURL = models.TextField(default="")
    text_reviews_count = models.TextField(default="")
    average_rating = models.TextField(default="")
    num_pages = models.TextField(default="")
    intro = models.TextField(default="")

    def __str__(self):
        return self.no


class AllBook(models.Model) :
    no = models.IntegerField(primary_key=True)
    bookname = models.TextField(default="")
    author = models.TextField(default="")
    publisher = models.TextField(default="")
    publication_year = models.TextField(default="")
    isbn13 = models.TextField(default="")
    addition_symbol = models.TextField(default="")
    vol = models.TextField(default="")
    class_no = models.TextField(default="")
    loan_count = models.TextField(default="")
    bookImageURL = models.TextField(default="")
    text_reviews_count = models.TextField(default="")
    average_rating = models.TextField(default="")
    num_pages = models.TextField(default="")
    intro = models.TextField(default="")

    def __str__(self):
        return self.no
