from django.urls import include, path
from django.contrib.auth import views as AuthView
from django.contrib.auth.views import  PasswordResetConfirmView


# from .forms import LoginForm
from .import views
urlpatterns = [
    path('register', views.signup, name='register'),
    path('account/login/',views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    # path('password_reset/', include('django.contrib.auth.urls'), name='password_reset'),
    path('modify/', views.update_password, name='modify'),
    path('forget/', views.forget, name='forget'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),





   
    # Réinitialisation de mot de passe

  
]

