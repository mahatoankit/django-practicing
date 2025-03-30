from django.urls import path
from .views import events, eventLandingPage, postEvents, editEventDetail, delete_event

urlpatterns = [
    path('', eventLandingPage, name='eventlandingPage'),
    path('post-events/', postEvents, name='postEvents'),
    path('edit-event/<int:eventId>/', editEventDetail, name='edit_event'),
    path('delete-event/<int:eventID>/', delete_event, name='delete_event'),
]