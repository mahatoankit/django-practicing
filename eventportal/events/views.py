from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from .models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User
from datetime import datetime

# Add these imports for DRF
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import EventSerializer


# Fix the permission class name here
class EventViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows events to be viewed or edited.
    """

    queryset = Event.objects.all().order_by("-created_at")
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Fix this line


@api_view(["GET"])
def api_event_list(request):
    """API endpoint to get all events"""
    events = Event.objects.all().order_by("-created_at")
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def api_event_detail(request, pk):
    """API endpoint to get a specific event"""
    try:
        event = Event.objects.get(pk=pk)
    except Event.DoesNotExist:
        return Response(status=404)

    serializer = EventSerializer(event)
    return Response(serializer.data)


def events(request):
    return HttpResponse("<h1>This is event section</h1>")


def eventLandingPage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        return HttpResponse(f"Thank you {name} for registering")
    else:
        return render(request, "events/index.html")


@login_required
def postEvents(request):
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
    return render(request, "events/postEvents.html", {"events": events})


# def delete_event(request, event_id):
#     event = Event.objects.get(id = event_id)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('postEvents')
#     return render(request, 'events/deleteEvent.html', {'event': event})


@login_required
def delete_event(request, eventID):
    event = Event.objects.get(id=eventID)
    event.delete()
    return redirect("postEvents")


@login_required
def editEventDetail(request, eventId):
    event = Event.objects.get(id=eventId)
    if request.method == "POST":
        title = request.POST.get("title")
        date_str = request.POST.get("date")
        location = request.POST.get("location")
        description = request.POST.get("description")
        capacity = request.POST.get("capacity")

        event.title = title
        event.location = location
        event.description = description
        event.capacity = capacity
        event.save()

        return redirect("postEvents")

    return render(request, "events/editEvents.html", {"event": event})


from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)  # Use the renamed function
    return redirect('eventlandingPage')