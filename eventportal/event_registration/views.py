from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Registration

# Create your views here.
def eventRegistration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        return HttpResponse(f'Thankyou {name} for registering')
    else:
        return render(request, 'event_registration/forms.html', {'registration':Registration})
    
def registrationList(request):
    registration = Registration.objects.get()
    return render(request, 'event_registration/registration_list.html', {'registration': registration})


def registrationDetail(request, id):
    registration = Registration.objects.get(id = id)
    return render (request, 'event_registration/registration_detail.html', {'registration': registration})

def registrationDelete(request, id):
    registration = Registration.objects.get(id = id)

    if request.method == 'POST':
        registration.delete()
        return redirect('registration-list')
    return render(request, 'event_registration/registration_delete.html', {'registration': registration})
