from django.db import models
from categories.models import Category as CategoryModel
from django.contrib.auth.models import User as UserModel
# Create your models here.


class Book(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField(null=True)
    author=models.CharField(max_length=150,null=True)
    add_date=models.DateTimeField(auto_now_add=True,null=True)
    borrow_price=models.DecimalField(decimal_places=2,max_digits=12,null=True)
    book_image=models.ImageField(upload_to="book_image",null=True)
    added_by=models.ForeignKey(UserModel,related_name="user_add",on_delete=models.CASCADE)
    category=models.ManyToManyField(CategoryModel,related_name="book_categories")
    quantity=models.IntegerField(null=True)
    total_borrowed_time=models.IntegerField(default=0,null=True)


