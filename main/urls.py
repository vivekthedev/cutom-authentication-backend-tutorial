from django.urls import path
from .views import HomeView
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", HomeView.as_view(), name='home'),
    path("login", LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("logout", LogoutView.as_view(), name='logout')
]