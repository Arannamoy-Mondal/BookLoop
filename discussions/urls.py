from django.urls import path
from .views import createDiscussion

urlpatterns=[
    path("create/<int:id>",createDiscussion,name="create_discussion")
]