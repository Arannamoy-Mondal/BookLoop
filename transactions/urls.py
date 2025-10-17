from django.urls import path,include
from .views import transactionHistoryView
urlpatterns=[
    path("transaction_history/",transactionHistoryView,name="transaction_history")
]