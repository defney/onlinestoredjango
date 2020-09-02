# dappx/forms.py
from django import forms
from dappx.models import UserProfileInfo
from django.contrib.auth.models import User
from dappx.models import products, Comment
import django_filters
from django.contrib.auth.forms import UserChangeForm

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'first_name', 'last_name','password','email')

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('age', 'gender','address', 'city', 'country')
        

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')
        #, 'age', 'gender', 'address', 'city', 'country'

class CommentForm(django_filters.FilterSet):
    class Meta():
        model = Comment
        fields = ('subject','comment', 'rate') 
