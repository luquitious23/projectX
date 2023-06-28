from django.db import models

# Create your models here.

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)


class MyData(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.TextField()
    # Add other fields as needed