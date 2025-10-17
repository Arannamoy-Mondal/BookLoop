from django.contrib import admin
from .models import Borrow_record 
# Register your models here.
class BorrowRecordAdmin(admin.ModelAdmin):
    list_display=['user__first_name','user__last_name','book','borrow_date','return_date']
admin.site.register(Borrow_record,BorrowRecordAdmin)