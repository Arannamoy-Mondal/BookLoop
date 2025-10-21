from django.shortcuts import render,redirect
from .models import Transaction
# Create your views here.


def transactionHistoryView(request):
    if request.user.is_authenticated:
        transactions=Transaction.objects.filter(user=request.user).order_by('-created_at')
        return render(request,'transactions_history.jinja',{"transactions":transactions})
    else:
        return redirect('login')