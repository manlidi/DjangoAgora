from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login
from .models import *
import re

# Create your views here.

def home(request):
    username = username = request.user.username
    return render(request, 'home.html', {'username':username})


def chat(request):
    return render(request, 'chat.html')


def vocal(request):
    return render(request, 'vocal.html')


def inscription(request):
    if request.method == "POST":
        email=request.POST.get('email')
        username=request.POST.get('username')

        adresse=request.POST.get('adresse')
        photo=request.FILES['photo']

        passe=request.POST.get('pass')
        c_pass=request.POST.get('c_pass')
        pattern = r'^[a-zA-Z0-9\-_]+$'

        if re.match(pattern, username):
            if Users.objects.filter(username=username).count()==0:
                if len(passe)>=6 :
                    if passe==c_pass:
                        user=Users.objects.create_user(email=email,adresse=adresse,photo=photo,username=username,password=passe)
                        user.set_password(passe)
                        user.is_active = True
                        user.save()
                        login(request, user) 
                        return redirect('home')

                    else:
                        messages.error(request,'le mot de passe doit etre identique ')
                else:
                    messages.error(request,'Le mot de passe doit avoir au moin 6 caractere')
            else:
                messages.error(request,'Cet username existe déja ')
            
        else:
                messages.error(request,'Le username ne doit pas contenir des caractères speciaux sauf - ou _')
            
    return render(request, 'inscription.html')


def connexion(request):
    if request.method == "POST":   
        username = request.POST.get('username')
        password = request.POST.get('password')
                
        user = Users.objects.filter(username=username).first() 
        
        if user is not None:    
            if user.check_password(password):
                login(request, user)            
                return redirect('home')
            else:
                 messages.error(request, "Mot de passe non valide")
        else:
            messages.error(request,"Username ou mot de passe non valide")      
    return render(request, 'connexion.html')