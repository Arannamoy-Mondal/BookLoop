from django.db import models
from django.contrib.auth.models import User as UserModel
from CONSTANT import TRANSACTION_TYPE,PAYMENT_STATUS
# Create your models here.
class Transaction(models.Model):
      user=models.ForeignKey(UserModel,related_name="user_transaction",on_delete=models.CASCADE)
      amount=models.FloatField(null=True)
      transaction_type=models.CharField(choices=TRANSACTION_TYPE,null=True)
      payment_status=models.CharField(choices=PAYMENT_STATUS,null=True)
      created_at=models.DateTimeField(auto_now=True,null=True)
      reference=models.CharField(max_length=500,null=True)
      