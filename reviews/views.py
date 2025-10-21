from django.shortcuts import render,redirect
from .models import Review
from borrow_records.models import Borrow_record
# Create your views here.


def createReview(r,id):
    if r.user.is_authenticated:
        if r.method=="POST":
            data=r.POST
            user=r.user
            borrow_record=Borrow_record.objects.get(pk=id)
            book=borrow_record.book
            rating=data['rating']
            if int(rating)==5:
                rating="⭐⭐⭐⭐⭐"
            elif int(rating)==4:
                rating="⭐⭐⭐⭐"
            elif int(rating)==3:
                rating="⭐⭐⭐"
            elif int(rating)==2:
                rating="⭐⭐"
            else:
                rating="⭐"
            
            comment=data['comment']
            review_image=r.FILES.get('review_image')
            # print(user,borrow_record,book,rating,comment,review_image)
            if review_image:
                Review.objects.create(user=user,book=book,borrow_record=borrow_record,rating=rating,comment=comment,review_image=review_image)
            else:
               Review.objects.create(user=user,book=book,borrow_record=borrow_record,rating=rating,comment=comment) 
            borrow_record.review_status=True
            borrow_record.save()
            return redirect('borrow_history')
    else:
        return redirect('login')


def reviewHistory(r):
    if r.user.is_authenticated:
       reviews=Review.objects.filter(user=r.user)
       return render(r,"review_history.html",{"reviews":reviews})
    else:
        return redirect("login")
    
    
def allReviewHistory(r):
    if r.user.is_authenticated and (r.user.user_acc.user_type=="ADMINISTRATOR" or r.user.user_acc.user_type=="SUPER_USER"):
       reviews=Review.objects.all()
       return render(r,"review_history.html",{"reviews":reviews})
    else:
        return redirect("login")

def deleteReview(r,id):
    if r.user.is_authenticated:
        review=Review.objects.get(pk=id)
        if review.user==r.user:
            review.delete()
            redirect("all_review_history")
        redirect("all_review_history")
    return redirect("home")