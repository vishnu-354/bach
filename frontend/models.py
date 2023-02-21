from django.db import models

# Create your models here.
class customerdb(models.Model):
    name= models.CharField(max_length=100, null=True, blank=True)
    email= models.EmailField(null=True, blank=True)
    password= models.IntegerField(null=False)
    cpassword=models.IntegerField(null=False)

class reviewdb(models.Model):
    Name = models.CharField(max_length=100,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Message = models.TextField(null=False, blank=False)

class deliverydb(models.Model):
    Products = models.CharField(max_length=100,null=True, blank=True)
    Name = models.CharField(max_length=100,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Ph_no = models.IntegerField(null=False)
    Address = models.CharField(max_length=100,null=True, blank=True)
    qty = models.IntegerField(null=False)
    totalprice = models.IntegerField(null=False)
