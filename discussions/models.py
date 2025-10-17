from django.db import models
from django.contrib.auth.models import User
from books.models import Book
# Create your models here.

class Discussion(models.Model):
    user=models.ForeignKey(User,related_name="user_discussions",on_delete=models.CASCADE)
    book=models.ForeignKey(Book,related_name="book_discussions",on_delete=models.CASCADE)
    comment=models.TextField(null=True)
    discussion_image=models.ImageField(upload_to="discussion_image",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
