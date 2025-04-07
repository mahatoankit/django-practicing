from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'events', views.EventViewSet)

urlpatterns = [
    # ViewSet-based URLs
    path('', include(router.urls)),
    
    # Function-based URLs (alternative)
    path('events-list/', views.api_event_list, name='api-event-list'),
    path('events-detail/<int:pk>/', views.api_event_detail, name='api-event-detail'),
]