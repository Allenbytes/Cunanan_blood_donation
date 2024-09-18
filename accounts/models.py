from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

# accounts/models.py

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, is_active=True, is_staff=False, is_superuser=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser
        )
        user.set_password(password)  # Ensure password is hashed
        user.save(using=self._db)
        return user


    def create_superuser(self, email, username, password=None):
        return self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            is_superuser=True
        )

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)  # Changed from is_admin to is_superuser

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        # Implement custom permission logic if needed
        return True

    def has_module_perms(self, app_label):
        # Implement custom module permissions if needed
        return True

    def set_password(self, raw_password):
        super().set_password(raw_password)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    height = models.DecimalField(max_digits=5, decimal_places=2)
    region = models.CharField(max_length=100)
    province = models.CharField(max_length=100)
    municipality = models.CharField(max_length=100)
    blood_type = models.CharField(max_length=3)
    availability = models.BooleanField(default=False)
    last_donation_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
