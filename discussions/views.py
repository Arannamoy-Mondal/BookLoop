from django.shortcuts import render,redirect
from .models import Discussion as DiscussionModel
from books.models import Book as BookModel
# Create your views here.


def createDiscussion(r,id):
    if r.user.is_authenticated:
        if r.method=="POST":
            data=r.POST
            discussion_image=r.FILES.get('discussion_image')
            comment=data["comment"]
            book=BookModel.objects.get(pk=id)
            if comment or discussion_image:
               print(comment)
               DiscussionModel.objects.create(user=r.user,comment=comment,discussion_image=discussion_image,book=book)
            return redirect("specific_book",id=id)
        else:
            return redirect("specific_book",id=id)
    else:
        return redirect("login")