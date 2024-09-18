from django.db import models
from accounts.models import User

class BloodDonationRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blood_requests')
    request_type = models.CharField(max_length=10, choices=(('donation', 'Donation'), ('looking', 'Looking')))
    blood_type = models.CharField(max_length=3)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
