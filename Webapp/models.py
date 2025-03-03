from django.db import models

# Create your models here.
class ContactDb(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    email=models.CharField(max_length=100,null=True,blank=True)
    message=models.TextField(max_length=200,null=True,blank=True)
