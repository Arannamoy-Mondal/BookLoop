from django.db import models
from django.contrib.auth.models import User as UserModel
from books.models import Book as BookModel
from CONSTANT import RETURN_STATUS
from django.utils import timezone
import datetime
# Create your models here.
class Borrow_record(models.Model):
    user = models.ForeignKey (UserModel,related_name="user_borrow_record",on_delete=models.CASCADE)
    book = models.ForeignKey(BookModel,on_delete=models.CASCADE)
    borrow_date=models.DateTimeField(null=True)
    return_status=models.CharField(choices=RETURN_STATUS,null=True)
    due_date=models.DateTimeField(null=True)
    return_date =models.DateTimeField(null=True,blank=True)
    created_at =models.DateTimeField(auto_now=True,null=True)
    review_status=models.BooleanField(default=False)
    @property
    def remaining_days(self):
        if self.due_date and self.borrow_date:
            borrow = timezone.make_aware(self.borrow_date) if timezone.is_naive(self.borrow_date) else self.borrow_date
            due = timezone.make_aware(self.due_date) if timezone.is_naive(self.due_date) else self.due_date
            delta = due - borrow
            return delta.days
        return None