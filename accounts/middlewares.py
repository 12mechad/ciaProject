from django.contrib.auth import logout
from django.utils import timezone
from datetime import timedelta
import json

class AutoLogoutMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Vérifier si l'utilisateur est authentifié
        if request.user.is_authenticated:
            # Vérifier si la dernière activité de l'utilisateur est enregistrée dans la session
            last_activity_str = request.session.get('last_activity')
            if last_activity_str:
                # Convertir la représentation JSON de la date en objet datetime
                last_activity = timezone.datetime.fromisoformat(json.loads(last_activity_str))
                # Calculer la durée écoulée depuis la dernière activité
                inactive_duration = timezone.now() - last_activity
                if inactive_duration > timedelta(minutes=15):
                    # Si la durée d'inactivité dépasse 15 minutes, déconnecter l'utilisateur
                    logout(request)

            # Enregistrer l'heure actuelle comme dernière activité de l'utilisateur
            request.session['last_activity'] = json.dumps(timezone.now().isoformat())

        return response
