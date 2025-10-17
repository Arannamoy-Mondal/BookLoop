from django.urls import path
from .views import getCategories,deleteCategory,updateCategory
urlpatterns=[
    path("get/",getCategories,name="get_categories"),
    path("update/<int:id>",updateCategory,name="update_category"),
    path("delete/<int:id>",deleteCategory,name="delete_category")
]