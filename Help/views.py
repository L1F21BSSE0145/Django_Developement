from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from Contact.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
      if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            message=request.POST.get("message")
        )
        messages.success(request, "Your message has been submitted successfully!")
        return redirect("contact")

      return render(request, "contact.html")

def signup(request):
      if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")   # ✅ THIS LINE
      
      return render(request, 'signup.html')

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)   # ✅ Django login
            return redirect("index")
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")

    return render(request, 'login.html')

