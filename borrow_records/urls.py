from django.urls import path
from .views import get_borrow_history
urlpatterns=[
    # path('create/',create,name=create),
    path('borrow_history/',get_borrow_history,name='borrow_history')
    
]