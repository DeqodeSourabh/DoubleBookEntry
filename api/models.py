from django.db import models


# Create your models here.
class Shelf(models.Model):
    shelfId = models.IntegerField()
    username = models.CharField(max_length=10)

class Books(models.Model):
    shelfId = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    bookId = models.IntegerField()
    balance = models.FloatField(default=0.0)

class Journal(models.Model):
    shelfId = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    journalId = models.IntegerField()
    status = models.CharField(max_length=10)
    metadata = models.CharField(max_length=10)

class BookEntity(models.Model):
    shelfId = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    journalId = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    bookId = models.ForeignKey(Shelf, on_delete=models.CASCADE)
    credit = models.FloatField(default=0.0)
    debit = models.FloatField(default= 0.0)
    creditSum = models.FloatField(default= 0.0)
    debitSum = models.FloatField(default= 0.0)
    toAdd = models.CharField(max_length=10)
    fromAdd = models.CharField(max_length=10)