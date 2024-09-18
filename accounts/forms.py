from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Profile
from django.contrib.auth import authenticate

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'availability', 'last_donation_date']
        widgets = {
            'last_donation_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_availability(self):
        availability = self.cleaned_data.get('availability')
        last_donation_date = self.cleaned_data.get('last_donation_date')
        if availability and last_donation_date:
            from datetime import datetime, timedelta
            today = datetime.now().date()
            if (today - last_donation_date).days < 56:
                raise forms.ValidationError(f"You need to wait {56 - (today - last_donation_date).days} more days before you can donate again.")
        return availability

# accounts/forms.py

from django import forms
from django.contrib.auth import authenticate

class CustomAuthenticationForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise forms.ValidationError("Invalid username or password")
            self.user_cache = user
        return cleaned_data

    def get_user(self):
        return getattr(self, 'user_cache', None)
