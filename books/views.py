from django.shortcuts import render,redirect,HttpResponse
from .models import Book as BookModel
from borrow_records.models import Borrow_record as BorrowRecordModel
from users.models import User as UserModel
from transactions.models import Transaction as TransactionModel
from categories.models import Category as CategoryModel
from discussions.models import Discussion as DiscussionModel 
from reviews.models import Review as ReviewModel
from django.utils import timezone
import datetime


def bookSection(r):
    if r.user.is_authenticated and (r.user.user_acc.user_type=="ADMINISTRATOR" or r.user.user_acc.user_type == "SUPER_USER"):
        books=BookModel.objects.all()
        return render(r,'books.html',{'books':books})
    else:
         return redirect('login')


def updateBook(r,id):
    if r.user.is_authenticated and (r.user.user_acc.user_type=="ADMINISTRATOR" or r.user.user_acc.user_type == "SUPER_USER"):
        book=BookModel.objects.get(pk=id)
        categories=CategoryModel.objects.all()
        #print(categories)
        not_selected_category=set(categories)-set(book.category.all())
        #print(not_selected_category)
        
        if r.method=="POST":
             data=r.POST
             book_image=r.FILES.get('book_image')
             if data['title']:
                book.title=data['title']
             if data['description']:
                book.description=data['description']
             if data['author']:
                 book.author=data['author']
             if book_image:
                 book.book_image=book_image
             if data['borrow_price']:
                 book.borrow_price=data['borrow_price']
             if data['quantity']:
                 book.quantity=data['quantity']
             if r.POST.getlist('category'):
                 new_categories=CategoryModel.objects.filter(title__in=r.POST.getlist('category'))
                 book.category.set(new_categories)
                 print(r.POST.getlist('category'))
                 print("New categories",new_categories)    
             book.save()
             return redirect('specific_book',book.id)
        return render(r,'add_book_form.html',{'book':book,'categories':not_selected_category})
    else:
         return redirect('login')
    

def deleteBook(r,id):
    if r.user.is_authenticated and (r.user.user_acc.user_type=="ADMINISTRATOR" or r.user.user_acc.user_type == "SUPER_USER"):
        book=BookModel.objects.get(pk=id)
        book.delete()
        return redirect('get-all-book','None')
    else:
         return redirect('login')

def addBook(r):
    if r.user.is_authenticated and (r.user.user_acc.user_type == "ADMINISTRATOR" or r.user.user_acc.user_type == "SUPER_USER"):
        categories = CategoryModel.objects.all()
        if r.method == "POST":
            data = r.POST
            book_image = r.FILES.get('book_image')
            book = BookModel.objects.create(
                title=data['title'],
                description=data['description'],
                author=data['author'],
                borrow_price=data['borrow_price'],
                book_image=book_image,
                added_by=r.user,
                quantity=data['quantity']
            )
            selected_categories= CategoryModel.objects.filter(title__in= r.POST.getlist('category'))
            book.category.set(selected_categories)
            book.save()

            return redirect('home')

        else:
            return render(r, 'add_book_form.html', {'categories': categories})
    else:
        return redirect('login')
          




def getAllBook(r,slug=None):
    if slug==None:
        books=BookModel.objects.all()
    books=BookModel.objects.all()
    return render(r,"books.html",{"books":books,"categorys":CategoryModel.objects.all()})

def getSpecificBook(r,id):
        book=BookModel.objects.get(pk=id)
        discussions=DiscussionModel.objects.filter(book=book)
        reviews=ReviewModel.objects.filter(book=book)
        return render(r,'book.html',{'book':book,'discussions':discussions,"reviews":reviews})
   

def borrowBook(r,id):
    if r.user.is_authenticated:
        book=BookModel.objects.get(pk=id)
        user=UserModel.objects.get(user=r.user)
        borrow = BorrowRecordModel.objects.filter(user=r.user,book=book,return_status="Not")
        if(user.balance<=book.borrow_price and user.balance<=(book.borrow_price+100)):
             return render(r,"failed_modal.html",{"message":"You do not have sufficient balance. Minimum balance must be 500."})
        if borrow:
             return render(r,"failed_modal.html",{"message":"You have already borrowed this book"})
        book.quantity-=1
        book.total_borrowed_time+=1
        book.save()
        user.balance-=book.borrow_price
        user.save()
        TransactionModel.objects.create(user=r.user,amount=book.borrow_price,transaction_type="Debit",payment_status="Success",reference=f"TXN{r.user.id}BB{TransactionModel.objects.count()}")
        borrow=BorrowRecordModel.objects.create(user=r.user,book=book,borrow_date=datetime.datetime.now(),due_date=datetime.datetime.now() + datetime.timedelta(days=7),return_status="Not")

        message=f"The book has been borrowed successfully. Your account has been updated, and the due date for return is {borrow.due_date.strftime('%d %b %Y')}."
        return render(r,"transaction_modal.html",{"message":message,"borrow":"borrow"})
    else:
        return redirect('login')
    

def returnBook(r,book_id,borrow_id):
        if r.user.is_authenticated:
            book=BookModel.objects.get(pk=book_id)
            user=UserModel.objects.get(user=r.user)
            borrow=BorrowRecordModel.objects.get(pk=borrow_id)
            book.quantity+=1
            book.save()
            late_days=max((timezone.now()-borrow.due_date).days,0)
            fine=max((late_days)*1,0)
            user.balance-=fine
            user.balance+=book.borrow_price
            user.save()
            borrow.return_status="Returned"
            borrow.return_date=timezone.now()
            borrow.save()
            TransactionModel.objects.create(user=r.user,amount=book.borrow_price,transaction_type="Credit",payment_status="Success",reference=f"TXN{r.user.id}RB{TransactionModel.objects.count()}")
            message = (
        f"Book returned successfully on {borrow.return_date.strftime('%d %b %Y')}. "
        f"Refunded amount: {book.borrow_price} Taka. "
        f"Late by {late_days} day(s), fine: {fine} Taka has been deducted.")
            return render(r,"transaction_modal.html",{"message":message,"return":"return"})
        else:
             return redirect('login')