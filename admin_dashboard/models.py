# admin_dashboard/models.py
from django.db import models
from django.conf import settings

class BloodDonationRequest(models.Model):
    REQUEST_TYPE_CHOICES = [
        ('donation', 'Donation'),
        ('looking', 'Looking')
    ]
    BLOOD_TYPE_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-')
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='admin_dashboard_blood_requests')
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES)
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPE_CHOICES)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.request_type} request by {self.user.username} for {self.blood_type}'

# Add other models if needed for admin functionalities
