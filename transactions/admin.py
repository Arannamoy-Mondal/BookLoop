from django.contrib import admin
from .models import Transaction
# Register your models here.
class TransactionAdmin(admin.ModelAdmin):
    list_display=('user__first_name','user__last_name','amount','transaction_type','created_at','reference')
admin.site.register(Transaction,TransactionAdmin)