from django.urls import path
from .views import createReview,reviewHistory,allReviewHistory
urlpatterns=[
    path("create/<int:id>",createReview,name="create_review"),
    path("review_history",reviewHistory,name="review_history"),
    path("all_review_history",allReviewHistory,name="all_review_history")
]