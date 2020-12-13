from django.db import models

# Create your models here.


class HealingBook(models.Model) :
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=30)
    keyword = models.CharField(max_length=500)
    image = models.CharField(max_length=200)
    review = models.CharField(max_length=1000)
    positive_score = models.FloatField(default=0)
    negative_score = models.FloatField(default=0)

    def __str__(self):
        return self.title
