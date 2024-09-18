from django import forms
from django.contrib.auth.forms import UserChangeForm
from accounts.models import User, Profile
from blood.models import BloodDonationRequest

class AdminUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'is_active', 'is_staff', 'is_superuser']

class AdminProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'weight', 'height', 'region', 'province', 'municipality', 'blood_type', 'availability']

class AdminBloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']
        widgets = {
            'request_type': forms.RadioSelect(choices=[('donation', 'Donation'), ('looking', 'Looking')]),
        }
