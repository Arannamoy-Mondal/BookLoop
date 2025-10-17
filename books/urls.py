from django.urls import path
from .views import getSpecificBook,borrowBook,returnBook,getAllBook,addBook,bookSection,deleteBook,updateBook

urlpatterns=[
    path("all-book/<slug:slug>",getAllBook,name="get-all-book"),
    path("<int:id>",getSpecificBook,name="specific_book"),
    path("borrow/<int:id>",borrowBook,name="borrow_book"),
    path("return/<int:book_id>/<int:borrow_id>",returnBook,name="return_book"),
    path("add_book",addBook,name="add_book"),
    path("book_section",bookSection,name="book_section"),
    path("update_book/<int:id>",updateBook,name="update_book"),
    path("delete_book/<int:id>",deleteBook,name="delete_book")
]