from django.contrib import admin
from .models import Review
# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display=["user__first_name","user__last_name","rating","comment","created_at"]

admin.site.register(Review,ReviewAdmin)
