from django.contrib import admin
from .models import User as UserModel
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display=('user_type','user__first_name','user__last_name','user__email','dob','contact_no','balance')
admin.site.register(UserModel,UserAdmin)