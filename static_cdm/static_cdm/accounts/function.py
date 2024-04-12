# functions.py

from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse

def send_password_reset_email(user, token):
    subject = 'Réinitialisation de mot de passe'
    message = f'Cliquez sur le lien suivant pour réinitialiser votre mot de passe: http://example.com{reverse("password_reset_confirm", args=[urlsafe_base64_encode(force_bytes(user.pk)), token])}'
    from_email = 'beninlan@ciagroup.com'
    to_email = user.email

    send_mail(subject, message, from_email, [to_email])
