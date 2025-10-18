from django.shortcuts import render,redirect,HttpResponse
from .models import User as UserModel
from django.contrib.auth.models import User
from transactions.models import Transaction as TransactionModel
from django.views.decorators.csrf import csrf_exempt
from dotenv import load_dotenv
import os
import requests
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages

load_dotenv()
Store_ID=os.getenv('Store_ID')
Store_Password=os.getenv('Store_Password')
issandbox=os.getenv('issandbox')
SSLZ_URL=os.getenv('SSLZ_URL')

def signUp(r):
   try:
      if r.user.is_authenticated:
        return redirect('home')
      else:
         if r.method=="POST":
            data=r.POST
            username=data["username"]
            first_name=data["first_name"]
            last_name=data["last_name"]
            contact_no=data["contact_no"]
            dob=data["dob"]
            gender=data["gender"]
            user_image=r.FILES.get('user_image')
            password1=data["password1"]
            password2=data["password2"]
            email=data["email"]

            if password1!=password2:
                messages.error(r,"Password does not match")
                print(username,first_name,last_name,email,password1,password2,dob,gender,user_image)
                return render(r,'signup.html')
            elif username and first_name and last_name and email and password1==password2 and dob and contact_no and gender and user_image:
               print(username,first_name,last_name,email,password1,password2,dob,gender,user_image)
               user1=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
               user2=UserModel.objects.create(user=user1,dob=dob,gender=gender,user_image=user_image,contact_no=contact_no)
               user=authenticate(r,username=username,password=password1)
               print(user)
               if user is not None:
                   login(r,user)
                   redirect('home')

            return redirect('home')
         else:
            return render(r,'signup.html')      
   except Exception as e:
         messages.error(r,e)
         return render(r,'signup.html')
      
def logIn(r):
    if r.user.is_authenticated:
        return redirect("home")
    else:
         if r.method=="POST":
             data=r.POST
             username=data['username']
             password=data['password']
             print(password)
             user=authenticate(request=r,username=username,password=password)
             if user is not None:
                login(request=r,user=user)
                return redirect("home")
             else:
                 messages.error(r, "Invalid username or password")
                 return render(r,"login_form_fun.html")
                 
         return render(r,"login_form_fun.html")
      

def logOut(r):      
    if r.user.is_authenticated: 
      logout(r)
      return redirect('home')
    else:
        redirect('login')


def updateUserProfile(r):
    if r.user.is_authenticated:
       if r.method=='POST':
            data=r.POST
            first_name=data['first_name']
            last_name=data['last_name']
            contact_no=data['contact_no']
            user_image=r.FILES.get('user_image')
            userC=UserModel.objects.get(user=r.user)
            userB=User.objects.get(pk=r.user.id)
            if first_name:
               userB.first_name=first_name
            if last_name:   
               userB.last_name=last_name
            userB.save()
            if contact_no:
               userC.contact_no=contact_no
            if user_image:
               userC.user_image=user_image
            userC.save()
            return redirect('update-profile-fun')
       else:
          return render(r,'update_profile_t.html')
    else:
         return redirect('login')
    



def depositView(request):
     print(request.user.is_authenticated)
     if request.user.is_authenticated:
          if request.method=="POST":
               data=request.POST
               if data['balance']:
                  balance=data['balance']
                  user=UserModel.objects.get(user=request.user)
               #    user.balance+=balance
               #    user.save()
               #    TransactionModel.objects.create(user=request.user,amount=balance,transaction_type="Credit",payment_status="Pending",reference=f"TXN{request.user.id}{TransactionModel.objects.count()}")

                  payload = {
                    "store_id": Store_ID,
                    "store_passwd": Store_Password,
                    "total_amount": balance,
                    "currency": "BDT",
                    "tran_id": f"TXN{request.user.id}{TransactionModel.objects.count()}",
                    "success_url": request.build_absolute_uri("payment/success/"),
                    "fail_url": request.build_absolute_uri("payment/fail/"),
                    "cancel_url": request.build_absolute_uri("payment/cancel/"),
                    "cus_name": request.user.username,
                    "cus_email": request.user.email,
                    "cus_add1": "Dhaka",
                    "cus_city": "Dhaka",  
                    "cus_country": "Bangladesh",
                    "cus_phone": user.contact_no,
                    "shipping_method": "NO",
                    "product_name": "Wallet Deposit",
                    "product_category": "Deposit",
                    "product_profile": "general",
                }
                  response = requests.post(SSLZ_URL, data=payload)
                  data = response.json()
                  if data.get("status") == "SUCCESS":
                    TransactionModel.objects.create(user=request.user,amount=balance,transaction_type="Credit",payment_status="Pending",reference=payload["tran_id"])
                    return redirect(data["GatewayPageURL"])
                  return redirect('home')
               else:
                    return render(request, "deposit_form.html")
          return render(request,'deposit_form.html',{'title':'BookLoop | Deposit'})
     else:
          return redirect('login')




@csrf_exempt
def payment_success(request):
    amount = request.POST.get("amount")
    tran_id = request.POST.get("tran_id") 
    transaction=TransactionModel.objects.get(reference=tran_id)
    user=UserModel.objects.get(user=transaction.user)
    user.balance+=int(amount.split(".")[0])
    user.save()
    transaction.payment_status="Success"
    transaction.save()

    return redirect('transaction_history')

@csrf_exempt
def payment_fail(request):
    amount = request.POST.get("amount")
    tran_id = request.POST.get("tran_id") 
    transaction=TransactionModel.objects.get(reference=tran_id)
    transaction.payment_status="Failed"
    transaction.save()
    return redirect('transaction_history')

@csrf_exempt
def payment_cancel(request):
    amount = request.POST.get("amount")
    tran_id = request.POST.get("tran_id") 
    transaction=TransactionModel.objects.get(reference=tran_id)
    transaction.payment_status="Cancelled"
    transaction.save()
    return redirect('transaction_history')






