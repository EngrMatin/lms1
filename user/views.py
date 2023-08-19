from django.shortcuts import render, redirect
from .forms import SignupForm, UserEditForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash


# Create your views here.

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            obj = SignupForm(request.POST)
            if obj.is_valid():
                obj.save()
                messages.success(request, 'Account created successfully')
                # print(obj.cleaned_data)
                return redirect("home")
        else:
            obj = SignupForm()        
                
        return render(request, 'signup_form.html', {'form':obj})
    
    else:
        return redirect("user_profile")
    

def show_user(request):
    if request.user.is_superuser:
        user = User.objects.all()
        return render(request, 'show_user.html', {'user_list':user})
    else:
        return redirect("home")

def edit_user(request, id):
    user = User.objects.get(pk=id)
    form = SignupForm(instance=user)
    if request.method == 'POST':
        obj = SignupForm(request.POST, instance = user)
        if obj.is_valid():
            print(obj.cleaned_data)
            obj.save()
            messages.success(request, 'Account edited successfully')
            return redirect("show_user")
    return render(request, 'signup_form.html', {'form':form})


def update_user(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = UserEditForm(request.POST, instance = request.user)
            if obj.is_valid():
                obj.save()
                messages.success(request, 'Account updated successfully')
                return redirect("user_profile")
        else:
            obj = UserEditForm(instance = request.user)
            
        return render(request, 'update_user.html', {'form':obj})
    
    else:
        return redirect("user_login")


def delete_user(request, id):
    user = User.objects.get(pk=id).delete()
    return redirect("show_user")

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            obj = AuthenticationForm(request=request, data = request.POST)
            if obj.is_valid():
                name = obj.cleaned_data['username']
                userpass = obj.cleaned_data['password']
                user = authenticate(username = name, password = userpass)
                if user is not None:
                    login(request, user)
                    return redirect("user_profile")
        else:
            obj = AuthenticationForm()    
                
        return render(request, 'user_login.html', {'form':obj})
    
    else:
        return redirect("user_profile")


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'user_profile.html', {'user':request.user})
    else:
        return redirect("user_login")

def user_logout(request):
    logout(request)
    return redirect("home")

def change_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = PasswordChangeForm(user=request.user, data=request.POST)
            if obj.is_valid():
                obj.save()
                update_session_auth_hash(request, obj.user)
                messages.success(request, 'Password has been changed successfully')
                return redirect("user_login")
        else:
            obj = PasswordChangeForm(user=request.user)        
                    
        return render(request, 'change_password.html', {'form':obj})
    
    else:
        return redirect("user_login")


def reset_password(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            obj = SetPasswordForm(user=request.user, data=request.POST)
            if obj.is_valid():
                obj.save()
                update_session_auth_hash(request, obj.user) 
                messages.success(request, 'Password has been reset successfully')
                return redirect("user_login")
        else:
            obj = SetPasswordForm(user=request.user)        
                    
        return render(request, 'change_password.html', {'form':obj})
    
    else:
        return redirect("user_login")
    
    