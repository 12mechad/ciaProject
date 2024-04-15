

from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from .managers import CustomUserManager  # Utilisation de la notation relative
from  ckeditor_uploader.fields import RichTextUploadingField


class AuteurUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    phone_regex = RegexValidator(regex=r'^\d{1,15}$',   message="Phone number should be exactly 10 digits")
    telephone = models.CharField(max_length=255, validators=[phone_regex], blank=True, null=True)
    biographie = RichTextUploadingField(blank=True, null=True)
    bibliographie = RichTextUploadingField(blank=True, null=True)
    images = models.ImageField(upload_to="images", blank=True, null=True)
    piece = models.FileField(upload_to="pdf_terrain", blank=True, null=True)
    is_auteur = models.BooleanField(default=False)
    is_proprietaire = models.BooleanField(default=False)
    is_ambassadeur = models.BooleanField(default=False)
    is_agent_immobiliere = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email



class PasswordResetToken(models.Model):
    user = models.OneToOneField(AuteurUser, on_delete=models.CASCADE)
    token = models.CharField(max_length=255)
    created_at = models.DateTimeField(default=timezone.now)

