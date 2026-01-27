from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import Account
from contacts.models import Contact
# HOME
def home(request):
    if not request.session.get('user_id'):
        return redirect('login')   # ❌ not logged in

    return render(request, 'home.html') # ✅ logged in
# ABOUT
def about(request):
    return render(request, 'about.html')


# CONTACT
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


# SIGNUP
def signup(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not full_name or not email or not password:
            return render(request, 'signup.html', {
                'error': 'All fields are required'
            })

        Account.objects.create(
            full_name=full_name,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


# LOGIN
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Account.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid credentials'
        })

    return render(request, 'login.html')

