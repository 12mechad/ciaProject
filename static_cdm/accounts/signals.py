from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

from .models import AuteurUser

@receiver(post_save, sender=AuteurUser)
def send_email_confirmation(sender, instance, created, **kwargs):
    if created:
        subject = 'Confirmation d\'e-mail'
        html_message = render_to_string('email_confirmation.html', {'user': instance})
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            html_message=html_message,
        )
