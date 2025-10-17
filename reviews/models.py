from django.db import models
from django.contrib.auth.models import User 
from books.models import Book
from borrow_records.models import Borrow_record
from CONSTANT import RATING
# Create your models here.

class Review(models.Model):
    user=models.ForeignKey(User,related_name="user_reviews",on_delete=models.CASCADE)
    book=models.ForeignKey(Book,related_name="book_reviews",on_delete=models.CASCADE)
    borrow_record=models.OneToOneField(Borrow_record,null=True,related_name="borrow_reviews",on_delete=models.CASCADE)
    rating=models.CharField(choices=RATING,null=True)
    comment=models.TextField(null=True,blank=True)
    review_image=models.ImageField(upload_to="review_image",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
