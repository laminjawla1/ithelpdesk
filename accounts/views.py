from django.shortcuts import render
from django.contrib.auth.models import auth
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.


def login(request):
    if request.user.is_authenticated:
        return redirect("/")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if password == "" and username == "":
            messages.info(request, "Fill blanks")
            return redirect("login")
        elif username == "":
            messages.info(request, "Enter User Name")
            return redirect("login")
        elif password == "":
            messages.info(request, "Enter Password")
            return redirect("login")
        elif user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid Credentials")
            return redirect("login")
    else:
        return render(request, 'login.html')


@login_required
def logout(request):
    auth.logout(request)
    return redirect("login")
