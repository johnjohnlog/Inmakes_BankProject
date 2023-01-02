from django.db import models

# Create your models here.
class Account(models.Model):
    name = models.CharField(max_length=250)
    age = models.IntegerField()
    date = models.DateField()
    address=models.TextField()
    phone=models.IntegerField()
    email=models.EmailField()
    def __str__(self):
        return self.name
