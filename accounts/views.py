from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from . forms import User_reg_form, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def signup_view(request):
    if request.method == 'POST':
        form = User_reg_form(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()  # form.save() returns the user
            login(request, user)
            user.save()
            messages.success(request, f'Thakyou for registering')
            return redirect('articles:list')
    else:
        form = User_reg_form()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()  # it puts the user from the form into variable 'user'
            login(request, user)  # logs the user in
            messages.success(request, f'Logged in as {user}!')
            if "next" in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    if request.method == 'POST':
        logout(request)
        messages.success(request, f'You have been Logged out')
        return redirect('articles:list')


@login_required(login_url="/accounts/login")
def profile(request):
    if request.method=='POST':
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                    request.FILES,
                                    instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated successfully')
            return redirect('accounts:profile')


    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)



    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'accounts/profile.html', context)
