from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from account.forms import UserRegisterForm
from account.models import Avatar


# Create your views here.

def editar_usuario(request):
    user = request.user

    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():
            info = form.cleaned_data

            user.username = info["username"]
            user.email = info["email"]
            user.avatar = info["imagen"]

            try:
                user.avatar.imagen = info["imagen"]
            except:
                avatar = Avatar(user=user, imagen=info["imagen"])
                avatar.save()

            user.save()
            return redirect("inicio")

    form = UserRegisterForm(initial={
        "username": user.username,
        "email": user.email,
        "imagen": user.avatar
    })

    context = {
        "form": form,
        "titulo": "Editar usuario",
        "enviar": "Editar"
    }
    return render(request, "account/form.html", context=context)



def register_account(request):
    if request.method == "POST":
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()
            return redirect(to='accountLogin')

    #form = UserCreationForm()

    form = UserRegisterForm()
    context = {
        "form": form,
        "titulo": "Registrar Usuario",
        "enviar": "Registrar"
    }
    return render(request, "account/form.html", context=context)



def login_account(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            info = form.cleaned_data

            user = authenticate(username=info["username"], password=info["password"])
            if user is not None:
                login(request, user)
                return redirect("inicio")
            else:
                return redirect("inicio")

    form = AuthenticationForm()
    context = {
        "form": form,
        "titulo": "Login",
        "enviar": "Iniciar"
    }
    return render(request, "account/form.html", context=context)
