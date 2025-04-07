from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    capacity = models.PositiveBigIntegerField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    @property
    def spots_left(self):
        """Returns the number of spots left for registration"""
        from event_registration.models import Registration

        registered = Registration.objects.filter(event=self).count()
        return max(0, self.capacity - registered)

    @property
    def is_full(self):
        """Returns True if the event is full"""
        return self.spots_left == 0
        
    def can_edit(self, user):
        """Check if user can edit this event"""
        return user.is_authenticated and (user == self.created_by or user.is_staff)