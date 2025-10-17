from django.urls import path,include
from .views import logIn,logOut,signUp,depositView,updateUserProfile,payment_success,payment_fail,payment_cancel

urlpatterns=[
    path('signup/',signUp,name='signup'),
    path("login/",logIn,name="login"),
    path('logout/',logOut,name='logout'),
    path('deposit/',depositView,name='deposit'),
    path('update-user-profile',updateUserProfile,name='update-profile-fun'),
    path("deposit/payment/success/", payment_success, name="payment_success"),
    path("deposit/payment/fail/", payment_fail, name="payment_fail"),
    path("deposit/payment/cancel/", payment_cancel, name="payment_cancel"),
    
]