from operator import mod
from django.db import models

# Create your models here.
class ware_house_model(models.Model):
    customer_name= models.CharField(max_length=100, default='')
    customer_id= models.CharField(max_length=20, default='')
    serial_number= models.CharField(max_length=20)
    height= models.FloatField(null= True)
    width= models.FloatField(null= True)
    length= models.FloatField(null= True)
    storage_space= models.FloatField(null= True)
    weight= models.IntegerField(null= True)
    storage_name= models.CharField(max_length=20)
    locate= models.CharField(max_length=15)
    date= models.DateField(null= True)
    description= models.CharField(max_length=30, default='')
    quantity= models.IntegerField(null= True)
    warehouse= models.CharField(max_length=20, default='')
    
    
    def __str__(self):
        return self.customer_name