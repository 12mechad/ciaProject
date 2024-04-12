from django.contrib import admin
from django.contrib.admin import AdminSite
from django.contrib.auth.admin import  UserAdmin
from django.contrib.auth.models import User
from .models import AuteurUser

# Register your models here.

    

    
AdminSite.site_header = "CIA Administration"

admin.site.register(AuteurUser)

