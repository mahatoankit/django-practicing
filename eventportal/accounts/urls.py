from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUpView, name='signup'),
    path('login/', views.loginView, name='login'),
    path('logout/', views.logout_view, name='logout'),  # Add this line
]