from django.shortcuts import render, redirect, HttpResponse

from .forms import UserProfileForm, UserForm, LoginForm
from django.contrib.auth.models import User

# login imports
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

# Create your views here.


def index(request):
    return render(request, 'users/index.html')


def register(request):
    registered = False

    form_user = UserForm(request.POST or None)
    form_profile = UserProfileForm(request.POST or None)
    if form_user.is_valid() and form_profile.is_valid():

        user = form_user.save()

        # if you don't use ModelForm, you need to get values
        # --------------------------------------------------
        # username = form_user.cleaned_data.get('username')
        # password = form_user.cleaned_data.get('password')
        # email = form_user.cleaned_data.get('email')

        # if you don't use UserCreationForm, you need to save db
        # ------------------------------------------------------
        # user = User(username=username, email=email)
        # if you send password to class directly like above, it will not hash pasword
        # to save password encrypted use the command below
        # user.set_password(password)

        # user.save()
        profile = form_profile.save(commit=False)
        profile.user = user

        if 'profile_pic' in request.FILES:
            profile.profile_pic = request.FILES['profile_pic']

        profile.save()
        messages.success(request, "Register successful")
        return redirect('index')

    context = {
        'form_profile': form_profile,
        'form_user': form_user
    }

    return render(request, 'users/register.html', context)


def user_login(request):

    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                messages.success(request, "Login successful")
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, "Account is not active")
                return render(request, 'users/user_login.html', {"form": form})
        else:
            messages.error(request, "Password or Username is wrong!")
            return render(request, 'users/user_login.html', {"form": form})
    return render(request, 'users/user_login.html', {"form": form})


@login_required
def user_logout(request):
    messages.success(request, "You Logout!")
    logout(request)
    return redirect('index')


@login_required
def students(request):
    return HttpResponse('<h1>Student Admin Page</h1>')

# Create your views here.
