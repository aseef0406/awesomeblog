from django.shortcuts import render,redirect

from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout


def creteUser(request):
    form=CreateUserForm
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Sucessfully Registered with usernames as "+user)
            return redirect('login')
    context={'form':form}
    return render(request,'registration/register.html',context)

def loginPage(request):
    if request=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect('register')
        else:
            messages.info(request,'Username or password is incorrect')
            return render(request, 'login.html')
    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('login')




