from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.auth.forms import AuthenticationForm
from django.utils import timezone
from .forms import UserRegistrationForm, ProfileForm
from .models import Profile
from django.contrib.auth import get_user_model

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            Profile.objects.create(user=user, weight=0.0, height=0.0)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

# accounts/views.py

from django.contrib.auth import login
from .forms import CustomAuthenticationForm

# accounts/views.py

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            print(f"Authenticated user: {user.username}")
            login(request, user)
            return redirect('profile')
        else:
            print(f"Form errors: {form.errors}")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


@login_required
def profile_view(request):
    profile = Profile.objects.filter(user=request.user).first()
    if not profile:
        return redirect('profile_update')
    return render(request, 'accounts/profile.html', {'profile': profile})

@login_required
def profile_update_view(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            updated_profile = form.save(commit=False)
            if updated_profile.availability:
                last_donation_date = updated_profile.last_donation_date
                if last_donation_date:
                    days_since_last_donation = (timezone.now().date() - last_donation_date).days
                    if days_since_last_donation < 56:
                        form.add_error('availability', f'You must wait {56 - days_since_last_donation} days before you can donate again.')
                        return render(request, 'accounts/profile_update.html', {'form': form})
            updated_profile.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile_update.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def base_view(request):
    return render(request, 'base.html')
