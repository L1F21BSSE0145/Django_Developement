from django.shortcuts import render
from django.contrib import messages
from .models import Contact

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        messages.success(request, "Your message has been submitted successfully")

    return render(request, 'contact.html')




