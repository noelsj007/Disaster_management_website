from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    
    username = None
    email = models.EmailField(('email address'), unique=True)
    mobile = models.CharField(max_length=15, null=True, blank= True)
    is_verified = models.BooleanField(default=False)
    forget_password = models.CharField(max_length=255, blank= True, null=True)
    location = models.PointField(null=True)
    address =  models.CharField(max_length=100, null=True)
    
    

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['mobile']

    objects = CustomUserManager()

    def __str__(self):
        return self.first_name

class Volunteer(models.Model):
    
    volunteer_email = models.EmailField(('email address'), unique=True)
    volunteer_mobile = models.CharField(max_length=15, null=True, blank= True)
    volunteer_address =  models.CharField(max_length=100, null=True)
    volunteer_skills = models.CharField(max_length=250, null=True)

class Service(models.Model):
    service_name = models.CharField(max_length=100, null= True)
    service_email = models.EmailField(('email address'), unique=True)
    service_mobile = models.CharField(max_length=15, null=True, blank= True)
    service_address =  models.CharField(max_length=100, null=True)
    service_type = models.CharField(max_length=250, null=True)

class ServiceAdmin(models.Model):
    serviceadmin_name = models.CharField(max_length=100)
    serviceadmin_locations = models.PointField(null=True)
    serviceadmin_address = models.CharField(max_length=100)
    serviceadmin_city = models.CharField(max_length=50)

    def __str__(self):
        return self.serviceadmin_name