from typing import Optional
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from .models import User

# Create your views here.


def user_list(request):
    users = User.objects.all()

    context = {
        "users": users,
    }

    return render(request, "user/user_list.html", context)


def login_view(request):
    error_message = None

    # Unbound state of our form
    form = AuthenticationForm()

    if request.method == "POST":
        # Bound state of our form
        form = AuthenticationForm(data=request.POST)
        # validation
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            # Authenticate user
            user: Optional[User] = authenticate(username=username, password=password)

            # Check if user was authenticated
            if user is not None:
                login(request, user)
                return redirect("profile")
        else:
            error_message = "Invalid username or password"

    context = {"form": form, "error_message": error_message}

    return render(request, "user/login.html", context)


def profile(request):
    return render(request, "user/profile.html")
