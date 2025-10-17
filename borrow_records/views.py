from django.shortcuts import render,redirect
from .models import Borrow_record
# Create your views here.
# def create(request,book):
#     Borrow_record.objects.create(user=request.user,book=book)
def get_borrow_history(request):
    if request.user.is_authenticated:
        b =  Borrow_record.objects.filter(user = request.user).order_by('-created_at')
        currently_reading=Borrow_record.objects.filter(user=request.user,return_status="Not").count()
        total_returned=b.count()-currently_reading
        return render (request,'borrow_record.html',{'b':b,"currently_reading":currently_reading,"total_returned":total_returned})  
    else:
        return redirect('home')
    