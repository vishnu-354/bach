from django.db import models

class admindb(models.Model):
    Name = models.CharField(max_length=100)
    Email = models.CharField(max_length=50)
    Mobileno = models.IntegerField(null=True)
    Password=models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)

class instrumentdb(models.Model):
    instrument = models.CharField(max_length=100)
    image = models.ImageField(null=True, blank=True)

class productdb(models.Model):
    instrument = models.CharField(max_length=100)
    Product = models.CharField(max_length=100)
    Quantity = models.IntegerField(null=True, blank=True)
    Price = models.IntegerField(null=True, blank=True)
    Description = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)
