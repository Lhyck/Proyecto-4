from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import logout

def index(request):
    return render(request,"core/index.html")

def contacto(request):
    return render(request,"core/contacto.html")

def acercaDe(request):
    return render(request,"core/acercade.html")

def iniciarSesion(request):
    print("Accediendo a la vista de inicio de sesión")
    return render(request,"core/login.html")

def exit(request):
    logout(request)
    return redirect('index')