from django.shortcuts import render,redirect
from django.http import JsonResponse
from .helper import askChatbot
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import IntegrityError


def SignUpPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password')
        pass2 = request.POST.get('confirm_password')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
        else:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'User already exists')
            else:
                try:
                    my_user = User.objects.create_user(username=uname, email=email, password=pass1)
                    my_user.save()
                    messages.success(request, 'Account created successfully')
                    return redirect('login')
                except IntegrityError:
                    messages.error(request, 'An error occurred while creating the account')

    return render(request, 'auth_system/signup.html')

def LoginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('password')
        user = authenticate(request,username=username,password=pass1)
        if user:
            login(request,user)
            return redirect('chatbot')
        else:
            messages.error(request, 'Invalid Credentials')
    return render(request,'auth_system/login.html')

@login_required(login_url='login')
def LogOutPage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def chatbot(request):
    if request.method == "POST":
        message = request.POST.get('message')
        response = askChatbot(message)
        return JsonResponse({'message': response})
    
    return render(request, "chatpage.html")

# Create your views here.
