from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from accounts.models import AuteurUser, PasswordResetToken
from accounts.forms import CustomUserCreationForm
from  accounts.function import send_password_reset_email
from .forms import CustomPasswordChangeForm, EmailAuthenticationForm, ForgetForm    
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Vous pouvez traiter les champs is_auteur ,  is_proprietaire, is_ambassadeur et is_agent_immobliere ici
            is_auteur = form.cleaned_data.get('is_auteur')
            is_proprietaire = form.cleaned_data.get('is_proprietaire')
            is_ambassadeur = form.cleaned_data.get('is_ambassadeur')
            is_agent_immobiliere = form.cleaned_data.get('is_agent_immobiliere')
            
            if is_auteur:
               
                pass
            if is_proprietaire:
                
                pass
            if is_ambassadeur:
                
                pass
            if is_agent_immobiliere:
                
                pass
            login(request, user)
            return redirect('login') 
        else:
            messages.error(request, form.errors) 
            
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {"form": form})


from django.contrib.auth import get_user_model
def login_user(request):
    next_url = request.GET.get('next')
    if request.method == 'POST':
        form = EmailAuthenticationForm(request.POST)
        email = request.POST.get('email')  # Correction ici
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)  # Correction ici
        print(user)
        
        if user:
            login(request, user)
            if isinstance(user, AuteurUser) and user.is_auteur:
                return redirect('auteur')
            elif isinstance(user, AuteurUser) and user.is_proprietaire:
                return redirect('compte')
            
            elif user.is_superuser :
                if not user.is_superuser :
                   return redirect('ambassadeur_immobiliere') 
                # Redirect superuser to the "departement" page
            return redirect('departement')
            
            
            if next_url and next_url.startswith('/'):
                return redirect(next_url)
    else:       
        form = EmailAuthenticationForm()
    return render(request, 'login.html', {"form": form})


@login_required
def update_password(request):
    
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST or None)
        print(form)
        if form.is_valid():
            form.save()
            # Ajoutez le code pour rediriger ou afficher un message de succès
            return redirect('login')
    else:
        form = CustomPasswordChangeForm(request.user)

    return render(request, 'update_password.html', {'form': form})



def logout_user(request):
    logout(request)
    return redirect('login')  # Redirige l'utilisateur vers la page de connexion


from django.db import IntegrityError

def forget(request):
    if request.method == 'POST':
        form = ForgetForm(request.POST)
        if form.is_valid():
            try:
                # Récupérer l'utilisateur par son adresse e-mail
                user = AuteurUser.objects.get(email=form.cleaned_data['email'])

                # Vérifier si un jeton existe déjà pour cet utilisateur
                password_reset_token = PasswordResetToken.objects.get(user=user)
                # Si un jeton existe, mettez à jour le jeton existant
                password_reset_token.token = default_token_generator.make_token(user)
                password_reset_token.save()
            except PasswordResetToken.DoesNotExist:
                # Si aucun jeton n'existe, créez un nouveau jeton
                token = default_token_generator.make_token(user)
                password_reset_token = PasswordResetToken.objects.create(user=user, token=token)

            # Envoyer l'e-mail avec le lien de réinitialisation
            send_password_reset_email(user, password_reset_token.token)

            # Rediriger l'utilisateur vers la page de connexion
            return redirect('login')  

    else:
        form = ForgetForm()

    return render(request, 'forget.html', {'form': form})


from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Vérifier si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Vérifier si la dernière activité de l'utilisateur est enregistrée dans la session
            last_activity = request.session.get('last_activity')
            if last_activity:
                # Calculer la durée écoulée depuis la dernière activité
                inactive_duration = timezone.now() - last_activity
                if inactive_duration > timedelta(minutes=15):
                    # Si la durée d'inactivité dépasse 15 minutes, déconnecter l'utilisateur
                    logout(request)

            # Enregistrer l'heure actuelle comme dernière activité de l'utilisateur
            request.session['last_activity'] = timezone.now()

        return response
