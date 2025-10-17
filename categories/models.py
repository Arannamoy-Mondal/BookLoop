from django.db import models
from django.contrib.auth.models import User as UserModel
# Create your models here.

class Category(models.Model):
      title=models.CharField(max_length=150,null=True)
      added_by=models.ForeignKey(UserModel,on_delete=models.CASCADE)
      add_date=models.DateTimeField(auto_now=True)
      slug=models.SlugField(max_length=100,null=True,unique=True,blank=True)
