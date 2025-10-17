from django.shortcuts import render,redirect
from .models import Category
from django.contrib import messages

def getCategories(r):
    if r.user.is_authenticated and r.user.user_acc.user_type=="ADMINISTRATOR":
       categories=Category.objects.all()
       if r.method=="POST":
          data=r.POST
          try:
              Category.objects.create(title=data['title'],added_by=r.user,slug=data['title'].lower())
          except Exception as e:
              messages.error(r,"Mostly duplicate category")
          return render(r,'category.html',{"categories":categories})
       return render(r,'category.html',{"categories":categories})
    else:
        return redirect('login')


def updateCategory(r,id):
    if r.user.is_authenticated and r.user.user_acc.user_type=="ADMINISTRATOR":
       categories=Category.objects.all()
       category=Category.objects.get(pk=id)
       
       if r.method=="POST":
          data=r.POST
          try:
              if data['title']:
                  category.title=data['title']
                  category.slug=data['title'].lower()
              category.save()
              return render(r,'category.html',{"categories":categories})
          except Exception as e:
              messages.error(r,"Mostly duplicate category")
          return render(r,'category.html',{"categories":categories})
       return render(r,'category.html',{"categories":categories,"category":category})
    else:
        return redirect('login')

def deleteCategory(r,id):
    if r.user.is_authenticated and r.user.user_acc.user_type=="ADMINISTRATOR":
        category=Category.objects.get(pk=id)
        category.delete()
        return redirect('get_categories')
    else:
        return redirect('login')