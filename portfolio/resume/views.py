from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    if request.method == "POST":
        contact = Contact()
        name = request.POST.get('name')
        email = request.POST.get('email')
        concern = request.POST.get('concern')
        contact.name = name
        contact.email = email
        contact.concern = concern
        contact.save()

        # Trigger SweetAlert popup
        messages.success(request, "Form submitted successfully.")  # Display a message for non-JS users
        return render(request, 'resume/home.html', {'submitted': True})

    return render(request, 'resume/home.html')
