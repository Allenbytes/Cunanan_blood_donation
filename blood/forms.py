from django import forms
from .models import BloodDonationRequest

class BloodDonationRequestForm(forms.ModelForm):
    class Meta:
        model = BloodDonationRequest
        fields = ['request_type', 'blood_type', 'region', 'province', 'municipality']
        widgets = {
            'request_type': forms.RadioSelect(choices=[('donation', 'Donation'), ('looking', 'Looking')]),
        }

    def __init__(self, *args, **kwargs):
        self.user_profile = kwargs.pop('user_profile', None)
        super().__init__(*args, **kwargs)
        if self.user_profile:
            if self.user_profile.availability:
                if self.instance and self.instance.request_type == 'donation':
                    self.fields['blood_type'].widget.attrs['readonly'] = True
                    self.fields['region'].widget.attrs['readonly'] = True
                    self.fields['province'].widget.attrs['readonly'] = True
                    self.fields['municipality'].widget.attrs['readonly'] = True
                    self.fields['blood_type'].initial = self.user_profile.blood_type
                    self.fields['region'].initial = self.user_profile.region
                    self.fields['province'].initial = self.user_profile.province
                    self.fields['municipality'].initial = self.user_profile.municipality
            else:
                if self.instance and self.instance.request_type == 'donation':
                    self.fields['blood_type'].widget.attrs['readonly'] = True
                    self.fields['region'].widget.attrs['readonly'] = True
                    self.fields['province'].widget.attrs['readonly'] = True
                    self.fields['municipality'].widget.attrs['readonly'] = True

class BloodDonationRequestUpdateForm(BloodDonationRequestForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.request_type == 'donation':
            self.fields['request_type'].widget = forms.HiddenInput()
