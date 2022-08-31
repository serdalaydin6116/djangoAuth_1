from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

​
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
​
class UserForm(UserCreationForm):
    class Meta():
        model = User
        fields = ('username', 'email')  
​
# class UserForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput())
​
    # class Meta():
        # model = User
        # fields = ('username', 'email', 'password')
​
class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        # fields = '__all__'
        exclude = ('user',)