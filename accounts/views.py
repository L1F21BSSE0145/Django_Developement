from django.shortcuts import redirect
from django.shortcuts import render, redirect
from accounts.models import Account

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

        if Account.objects.filter(email=email).exists():
            return render(request, 'signup.html', {
                'error': 'Email already exists'
            })

        Account.objects.create(
            full_name=full_name,
            email=email,
            password=password
        )

        return redirect('login')

    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = Account.objects.filter(email=email, password=password).first()

        if user:
            request.session['user_id'] = user.id
            request.session['user_name'] = user.full_name
            return redirect('home')

        return render(request, 'login.html', {
            'error': 'Invalid email or password'
        })

    return render(request, 'login.html')