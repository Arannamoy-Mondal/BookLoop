from django.contrib import admin
from .models import Discussion
# Register your models here.

class DiscussionAdmin(admin.ModelAdmin):
    list_display=["user__first_name","user__last_name","comment","created_at"]

admin.site.register(Discussion,DiscussionAdmin)