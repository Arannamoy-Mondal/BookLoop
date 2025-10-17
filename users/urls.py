from django.urls import path,include
from .views import LogInView,LogOutView,SignUpView,depositView,UserUpdateView,updateUserProfile,payment_success,payment_fail,payment_cancel,login_fun

urlpatterns=[
    path('login/',login_fun,name="login"),
    path('signup/',SignUpView.as_view(),name='signup'),
    path('logout/',LogOutView.as_view(),name='logout'),
    path('update-profile/',UserUpdateView.as_view(),name='update-profile'),
    path('deposit/',depositView,name='deposit'),
    path('update-user-profile',updateUserProfile,name='update-profile-fun'),
    path("deposit/payment/success/", payment_success, name="payment_success"),
    path("deposit/payment/fail/", payment_fail, name="payment_fail"),
    path("deposit/payment/cancel/", payment_cancel, name="payment_cancel"),

    path("loginf/",login_fun,name="login-fun")
]