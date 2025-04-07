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
        description = request.POST.get("description")
        date = request.POST.get("date")
        location = request.POST.get("location")
        capacity = request.POST.get("capacity")

        event = Event(
            title=title,
            description=description,
            date=date,
            location=location,
            capacity=capacity,
            created_by=request.user  # Set the current user as creator
        )
        event.save()
        messages.success(request, "Event created successfully!")
        return redirect("postEvents")

    events = Event.objects.all().order_by('-created_at')
    return render(request, "events/postEvents.html", {"events": events})


# def delete_event(request, event_id):
#     event = Event.objects.get(id = event_id)
#     if request.method == 'POST':
#         event.delete()
#         return redirect('postEvents')
#     return render(request, 'events/deleteEvent.html', {'event': event})


@login_required
def delete_event(request, eventID):
    event = get_object_or_404(Event, id=eventID)
    
    # Check if user is authorized to delete this event
    if not event.can_edit(request.user):
        messages.error(request, "You don't have permission to delete this event.")
        return redirect("postEvents")
    
    if request.method == "POST":
        event.delete()
        return redirect("postEvents")
    
    return render(request, "events/delete_confirm.html", {"event": event})


@login_required
def editEventDetail(request, eventId):
    event = get_object_or_404(Event, id=eventId)
    
    # Check if user is authorized to edit this event
    if not event.can_edit(request.user):
        messages.error(request, "You don't have permission to edit this event.")
        return redirect("postEvents")
    
    if request.method == "POST":
        # Process form submission
        event.title = request.POST.get("title")
        event.description = request.POST.get("description")
        event.date = request.POST.get("date")
        event.location = request.POST.get("location")
        event.capacity = request.POST.get("capacity")
        event.save()

        return redirect("postEvents")

    return render(request, "events/editEvents.html", {"event": event})


from django.contrib.auth import logout as auth_logout

def logout_view(request):
    auth_logout(request)  # Use the renamed function
    return redirect('eventlandingPage')