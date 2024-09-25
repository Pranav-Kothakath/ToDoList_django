from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
from Users.models import Task

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Login(request):
    err_msg = None

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user and user.is_active:
            login(request, user)
            tasks = Task.objects.filter(user=request.user).order_by('complete_by_date') 
            return redirect('list_user_tasks')
        else:
            err_msg = 'Invalid credentials'
            
    return render(request, 'login.html', {'error': err_msg})

def Logout(request):
    logout(request)
    return redirect('home')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:
            # Return form values to the template along with the error message
            return render(request, 'signup.html', {
                'error': 'Passwords do not match',
                'username': username,
                'email': email,
                'password':password,
                'confirm_password': confirm_password,
            })
        
        try:
            User.objects.create_user(username=username, email=email, password=password)
        except ValidationError as e:
            return render(request, 'signup.html', {'error': str(e)})
        
        return redirect('login')

    return render(request, 'signup.html')