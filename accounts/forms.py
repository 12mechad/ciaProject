from multiprocessing import AuthenticationError
from django import forms
from .models import AuteurUser
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import AuthenticationForm




class CustomUserCreationForm(UserCreationForm):
        is_auteur = forms.BooleanField(required=False, initial=False)
        is_proprietaire = forms.BooleanField(required=False, initial=False)
        def __init__(self,*args, **kwargs):
              super().__init__(*args, **kwargs)
              self.fields["username"].widget.attrs.update({
                     'type':'text',
                     'class':'form-control round',
                     'id':'user-name',
                     'name':'prenom',
                     'placeholder':"Nom d'utilisateur",
                     'required':''
              })
              self.fields["last_name"].widget.attrs.update({
                     'type':'text',
                     'class':'form-control round',
                     'id':'user-name',
                     'name':'nom',
                     'placeholder':'Nom',
                     'required':''
              })
              self.fields["first_name"].widget.attrs.update({
                     'type':'text',
                     'class':'form-control round',
                     'id':'user-name',
                     'name':'prenom',
                     'placeholder':'Prénom',
                     'required':''
              })
              
              self.fields["email"].widget.attrs.update({
                     'type':'email',
                     'class':'form-control round',
                     'id':'user-email',
                     'name':'email',
                     'placeholder':'email',
                     'required':''
                     })
              self.fields["password1"].widget.attrs.update({
                     'type':'password',
                     'class':'form-control round',
                     'id':'user-passvword',
                     'name':'password1',
                     'placeholder':'Mot de passe',
                     'required':''
                     })
              self.fields["password2"].widget.attrs.update({
                     'type':'password',
                     'class':'form-control round',
                     'id':'user-password',
                     'name':'password2',
                     'placeholder':'Confirmer mot de passe',
                     'required':''
                     })       
        class Meta(UserCreationForm):
            model = AuteurUser
            fields = ['username', 'last_name', 'first_name', 'email', 'password1', 'password2', 'is_auteur', 'is_proprietaire','is_ambassadeur','is_agent_immobiliere']





class EmailAuthenticationForm(AuthenticationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'type': 'text',
            'class': 'form-control round',
            'id': 'user-name',
            'name': 'username',
            'placeholder': "Adresse e-mail",
            'required': ''
        })
        self.fields["password"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control round',
            'id': 'user-password',
            'name': 'password',
            'placeholder': 'Mot de passe',
            'required': ''
        })

    def clean(self):
        email = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if email and password:
            self.user_cache = authenticate(self.request, email=email, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': self.username_field.verbose_name},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

    class Meta:
        model = AuteurUser
        fields = ['email', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = AuteurUser
        fields = ('email',)





class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields["old_password"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control round',
            'id': 'user-password',
            'name': 'old_password',
            'placeholder': 'Ancien Mot de passe',
            'required': ''
        })
        
        self.fields["new_password1"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control round',
            'id': 'user-password',
            'name': 'new_password1',
            'placeholder': 'Nouveau Mot de passe',
            'required': ''
        })

        self.fields["new_password2"].widget.attrs.update({
            'type': 'password',
            'class': 'form-control round',
            'id': 'user-password',
            'name': 'new_password2',
            'placeholder': 'Confirmer Mot de passe',
            'required': ''
        })

    class Meta:
        model = get_user_model()  # Get the User model
        fields = ('old_password', 'new_password1', 'new_password2')
   


    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Ajoutez des règles de validation personnalisées pour l'e-mail si nécessaire
        return email

# forms.py

from django import forms
from django.contrib.auth.forms import PasswordResetForm

class ForgetForm(PasswordResetForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'autofocus': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({
            'type': 'text',
            'class': 'form-control round',
            'id': 'user-name',
            'name': 'username',
            'placeholder': "Adresse e-mail",
            'required': ''
        })

    class Meta:
        model = AuteurUser  # Remplacez YourUserModel par votre modèle utilisateur personnalisé
        fields = ["email"]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        # Ajoutez ici une logique de validation personnalisée pour l'adresse e-mail si nécessaire
        return email
