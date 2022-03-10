from operator import mod
from django.db import models

# Create your models here.
class ware_house_model(models.Model):
    customer_name= models.CharField(max_length=100)
    customer_id= models.CharField(max_length=20)
    serial_number= models.CharField(max_length=20)
    height= models.FloatField()
    width= models.FloatField()
    length= models.FloatField()
    storage_space= models.FloatField()
    weight= models.IntegerField()
    storage_name= models.CharField(max_length=20)
    locate= models.CharField(max_length=15)
    date= models.DateField()
    description= models.CharField(max_length=30)
    quantity= models.IntegerField()
    warehouse= models.CharField(max_length=20, default='')
