from django.shortcuts import render
from django.db import models
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        return render(request, "contact.html", {
            "success": "Your message has been submitted successfully!"
        })

    return render(request, "contact.html")
