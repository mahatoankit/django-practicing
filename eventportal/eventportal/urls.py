from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # This includes logout now
    path('event-registration/', include('event_registration.urls')),
    path('', include('events.urls')),
    path('api/', include('events.api_urls')),  # Don't forget this for your API
]