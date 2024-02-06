from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth import update_session_auth_hash
import csv, io



# Create your views here.
from .models import Score
from .models import Score_hist



    
    
       
    

# Create your views here.
def landingPage(request):
    return render(request, 'accounts/index.html')


def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = UserCreationForm()
        if request.method =='POST':
            form = (request.POST)
            if form.is_valid():
                user=form.save()
            
                username = form.cleaned_data.get('username')
                messages.success(request, f'Registration successful, you can now login in as {username}')
        
                messages.success(request, 'Hi!' + user +  'Your Account has been created successfully!')
            
                return redirect('login')       
        context = {'form':form}
        return render(request, 'accounts/register.html', context)        

def loginPage(request):
    if request.user.is_authenticated:
        messages.success(request, "Welcome!") 
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
        
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'username OR password is Incorrect')  
        context = {}
        return render(request, 'accounts/login.html', context) 

def logoutUser(request):
    logout(request)
    messages.success(request, "You Have Been Logged Out...")
    return redirect('landing')


@login_required(login_url='/login')
def home(request):
   
    scores = Score.objects.filter(user=request.user).order_by('id')
    return render(request, 'accounts/customer.html', {'scores':scores}) 
    



@login_required(login_url='/login')
def userPage(request):
    scored = request.user.customer.score_set.all()
    context ={'scored': scored}
    return render(request, 'accounts/customer.html', context)


@login_required(login_url='/login')  
def view_history(request):
    scoresi= Score_hist.objects.filter(user=request.user).order_by('id')
    return render(request, 'accounts/view_history.html', {'scoresi':scoresi})


    
@login_required(login_url='/login')
def score_hist(request, id):
    scored = Score.objects.get(pk=id)
   
    return render(request, 'accounts/customer.html', {'scored':scored, }) 






    
   

















