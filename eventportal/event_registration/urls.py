from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='event_list'),
    # Add this line to support the old URL name
    path('', views.event_list, name='eventRegistration'),  
    path('register/<int:event_id>/', views.register_event, name='register_event'),
    path('success/', views.registration_success, name='registration_success'),
]