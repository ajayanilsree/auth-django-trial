from django.shortcuts import render,redirect
from .forms import SignupForm,LoginForm
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout



def index(request):
    return render(request,'index.html')
def signup(request):
    form=SignupForm()
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('login') 
        
    return render(request,'signup.html',{'form':form})

def Login(request):
    form=LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()    
            auth_login(request, user) 
            messages.success(request, "Logged in successfully!")
            return redirect('dashboard')
    return render(request,'login.html',{'form':form})

def dashboard(request):
    return render(request,'dashboard.html')

def logout(request):
    auth_logout(request)
    return redirect('login')