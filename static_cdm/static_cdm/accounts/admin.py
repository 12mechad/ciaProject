# from django.contrib import admin
# from django.contrib.auth import get_user_model
# from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# from .models import AuteurUser


# from .forms import CustomUserCreationForm, CustomUserChangeForm

# User = get_user_model()

# # Supprimer le modèle de groupe de l'administrateur. Nous ne l'utilisons pas.

# class CustomUserAdmin(BaseUserAdmin):
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     model = User
#     list_display = ('email', 'is_staff', 'is_active',)
#     list_filter = ('email', 'is_staff', 'is_active',)
#     fieldsets = (
#         (None, {'fields': ('email', 'telephone', 'name','first_name','last_name', 'password','biographie','bibliographie','images','piece','is_auteur','is_proprietaire')}),
#         ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),   #'is_customer' , 'is_seller'
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'telephone', 'username','first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active','biographie','bibliographie','images','piece','is_auteur','is_proprietaire')}
#         ),
#     )
#     search_fields = ('email',)
#     ordering = ('email',)







# #admin.site.unregister(User)
# admin.site.register(AuteurUser, CustomUserAdmin)

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import AuteurUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class CustomUserAdmin(BaseUserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = AuteurUser  # Utilisez le modèle AuteurUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'telephone', 'username', 'first_name', 'last_name', 'password', 'biographie', 'bibliographie', 'images', 'piece', 'is_auteur', 'is_proprietaire')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'telephone', 'username', 'first_name', 'last_name', 'password1', 'password2', 'is_staff', 'is_active', 'biographie', 'bibliographie', 'images', 'piece', 'is_auteur', 'is_proprietaire')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(AuteurUser, CustomUserAdmin)
