from django.db import models

# Create your models here.
from django.core.mail import send_mail
from events.models import Event



class Registration(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.event.title}"

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            self.send_confirmation_email()

    def send_confirmation_email(self):
        subject=f"Registration for {self.event.title}"
        message=f"Hi {self.name}, \n\n You're registered for {self.event.title} on {self.event.date}"
        send_mail(subject, message, 'hamroevent@gmail.com', [self.email], fail_silently=False)