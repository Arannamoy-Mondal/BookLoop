from django.db import models
from books.models import Book
from django.contrib.auth.models import User
from CONSTANT import *
# Create your models here.


class User(models.Model):
    user=models.OneToOneField(User,related_name="user_acc",on_delete=models.CASCADE)
    email=models.EmailField(unique=True,null=True)
    contact_no=models.CharField(max_length=11,unique=True,null=True)
    borrowed_books=models.ManyToManyField(Book, related_name='borrowed_books', blank=True)
    gender=models.CharField(max_length=20,choices=GENDER,null=True)
    deposit_date=models.DateField(auto_now_add=True,null=True)
    balance=models.DecimalField(decimal_places=2,max_digits=12,default=0,null=True)
    dob=models.DateField(null=True)
    joining_time=models.DateTimeField(auto_now=True,null=True)
    user_image=models.ImageField(upload_to="user_image",null=True,blank=True)
    user_type=models.CharField(choices=USER_TYPE,null=True)

    def __str__(self):
        return f"{self.user.first_name}"