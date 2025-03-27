from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    capacity = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def is_full(self):
        return self.capacity <= self.registration_set.count() >= self.capacity