from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length = 30)
    author   = models.CharField(max_length = 20)
    num  = models.CharField(max_length = 40)
    p_date = models.CharField(max_length = 23)
    numOfCopies  = models.IntegerField()
    def __str__(self):
        return self.num