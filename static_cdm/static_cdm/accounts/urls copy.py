from django.urls import include, path
from django.contrib.auth import views as AuthView

# from .forms import LoginForm
from .import views
urlpatterns = [
    path('register', views.signup, name='register'),
    path('account/login/',views.login_user, name='login'),
    path('logout/', AuthView.LogoutView.as_view(next_page='login'), name='logout'), 
    path('password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    path('modify/', views.update_password, name='modify'),
   



   
    # Réinitialisation de mot de passe

  
]
