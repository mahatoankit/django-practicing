from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Registration
from events.models import Event
from django.utils import timezone
from django.contrib import messages


def listEvents(request, eventId):
    if request.method == "POST":
        title = request.POST.get("title")
        date_str = request.POST.get("date")
        location = request.POST.get("location")
        description = request.POST.get("description")
        capacity = request.POST.get("capacity")
        try:
            date = timezone.datetime.fromisoformat(date_str)
            if timezone.is_naive(date):
                date = timezone.make_aware(date)
        except (ValueError, TypeError):
            date = timezone.now()

        Event.objects.create(
            title=title,
            date=date,
            location=location,
            description=description,
            capacity=int(capacity),  # Convert to integer
        )
        return redirect("postEvents")  # Redirect after POST

    # For both GET and after redirect from POST
    events = Event.objects.all().order_by("-created_at")
    return render(request, "event_registration/eventsPage.html", {"events": events})


def event_list(request):
    """View to display all available events for registration"""
    events = Event.objects.all().order_by("date")
    return render(request, "event_registration/event_list.html", {"events": events})


def register_event(request, event_id):
    """View to register for a specific event"""
    event = get_object_or_404(Event, id=event_id)

    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")

        # Create registration
        registration = Registration(event=event, name=name, email=email)
        registration.save()

        # Show success message
        messages.success(request, f"You've successfully registered for {event.title}!")
        return redirect("event_list")

    return render(request, "event_registration/forms.html", {"event": event})


def registration_success(request):
    """View to display registration success page"""
    return render(request, "event_registration/success.html")


# Keep your existing eventRegistration view if you have one
def eventRegistration(request):
    """Legacy view - redirect to the event list"""
    return redirect("event_list")


def registrationList(request):
    registration = Registration.objects.get()
    return render(
        request,
        "event_registration/registration_list.html",
        {"registration": registration},
    )


def registrationDetail(request, id):
    registration = Registration.objects.get(id=id)
    return render(
        request,
        "event_registration/registration_detail.html",
        {"registration": registration},
    )


def registrationDelete(request, id):
    registration = Registration.objects.get(id=id)

    if request.method == "POST":
        registration.delete()
        return redirect("registration-list")
    return render(
        request,
        "event_registration/registration_delete.html",
        {"registration": registration},
    )
