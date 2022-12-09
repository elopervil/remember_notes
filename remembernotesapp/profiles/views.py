from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.


class RegisterView (View):

    def get(self, request):
        form = UserCreationForm()
        return render(request, "profiles/register.html", {
            "form": form
        })

    def post(self, request):
        form = UserCreationForm(request.POST)

        if (form.is_valid()):
            user = form.save()
            login(request, user)
            return redirect('notes:home')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])

            return render(request, "profiles/register.html", {
                "form": form
            })


def logout_view(request):
    logout(request)
    return redirect('profiles:login')


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usernam = form.cleaned_data.get("username")
            passw = form.cleaned_data.get("password")
            user = authenticate(username=usernam, password=passw)
            if user is not None:
                login(request, user)
                return redirect('notes:home')
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")

    form = AuthenticationForm()
    return render(request, "profiles/login.html", {
        "form": form
    })
