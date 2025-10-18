from django.urls import path,include
from .views import logIn,logOut,signUpUser,depositView,updateUserProfile,payment_success,payment_fail,payment_cancel,signUpSuperUser,allUserHistory,promoteAsAdministrator

urlpatterns=[
    path('signup/',signUpUser,name='signup'),
    path("login/",logIn,name="login"),
    path('logout/',logOut,name='logout'),
    path('deposit/',depositView,name='deposit'),
    path('update-user-profile',updateUserProfile,name='update-profile-fun'),
    path("deposit/payment/success/", payment_success, name="payment_success"),
    path("deposit/payment/fail/", payment_fail, name="payment_fail"),
    path("deposit/payment/cancel/", payment_cancel, name="payment_cancel"),
    path("superuser/signup/",signUpSuperUser,name="create-super-user"),
    path("all-user-history/",allUserHistory,name="all-user-history"),
    path("promoteAsAdministrator/<int:id>",promoteAsAdministrator,name="promotion")
]