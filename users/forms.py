from django import forms
from .models import User as UserModel
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from CONSTANT import *

class SignUpForm(UserCreationForm):
    gender=forms.ChoiceField(choices=GENDER)
    dob=forms.DateField()
    contact_no=forms.CharField()
    class Meta:
        model=User
        fields = ['username', 'first_name','last_name','email','password1', 'password2', 'gender','dob']
    
    def save(self, commit = True):
        user1 = super().save(commit=True)
        if commit == True:
            # user1.is_active=False
            user1.save()
            gender1 = self.cleaned_data.get('gender')
            dob1=self.cleaned_data.get('dob')
            contact_no1=self.cleaned_data.get('contact_no')
            email1=self.cleaned_data.get('email')
            print(gender1)
            UserModel.objects.create(user=user1,dob=dob1,email=email1,contact_no=contact_no1,gender=gender1)
        return user1
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['first_name'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
        )})

        self.fields['last_name'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['email'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['password1'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['password2'].widget.attrs.update({'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['dob'].widget=forms.DateInput(
        attrs=({
        'type': 'date',
        'class': (
        'appearance-none block w-full bg-gray-200 date'
        'text-gray-700 border border-gray-200 rounded '
        'py-3 px-4 leading-tight focus:outline-none '
        'focus:bg-white focus:border-gray-500'
        "hover:bg-white dark:bg-white dark:text-black"
         )
         })
        )

        self.fields['gender'].widget.attrs.update({
            'type':'select',
            'class': (
            'appearance-none block w-full bg-gray-200 '
            'text-gray-700 border border-gray-200 rounded '
            'py-3 px-4 leading-tight focus:outline-none '
            'focus:bg-white focus:border-gray-500'
            "hover:bg-white dark:bg-white dark:text-black"
            )})
        
        self.fields['contact_no'].widget=forms.DateInput(
        attrs=({
        'type': 'text',
        'class': (
        'appearance-none block w-full bg-gray-200 date'
        'text-gray-700 border border-gray-200 rounded '
        'py-3 px-4 leading-tight focus:outline-none '
        'focus:bg-white focus:border-gray-500'
        "hover:bg-white dark:bg-white dark:text-black"
         )
         })
        )


class DepositForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['balance']


class UserUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    gender = forms.ChoiceField(choices=GENDER)
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': (
                    'appearance-none block w-full bg-gray-200 '
                    'text-gray-700 border border-gray-200 rounded '
                    'py-3 px-4 leading-tight focus:outline-none '
                    'focus:bg-white focus:border-gray-500'
                    "hover:bg-white dark:bg-white dark:text-black"
                )
            })
        # jodi user er account thake 
        if self.instance:
            try:
                user_account = self.instance.user_acc
            except UserModel.DoesNotExist:
                user_account = None
                user_address = None

            if user_account:
                self.fields['gender'].initial = user_account.gender

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_account, created = UserModel.objects.get_or_create(user=user) 
            user_account.gender = self.cleaned_data['gender']
            user_account.save()
        return user        