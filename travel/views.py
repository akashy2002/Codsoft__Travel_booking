from django.shortcuts import render, redirect, HttpResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'index.html')


def booking(request, uid):
    flight_obj = Flight.objects.get(uid=uid)
    if request.method == 'POST':
        book_date = request.POST.get('dates')
        gender = request.POST.get('gender')
        Class = request.POST.get('class')
        myuser = request.user
        flight = Flight.objects.get(uid=uid)

        book_obj = Flightbooking(
            Name=flight, start_date=book_date, Class=Class, Gender=gender, user=myuser)
        book_obj.save()
        messages.success(request, "Congrats! Your ticket has been booked!")
        return redirect("bookings")

    context = {'flight_obj': flight_obj}
    return render(request, 'book.html', context=context)


def bookings(request):
    if request.user.is_authenticated:
        user = request.user
        flight_bookings = Flightbooking.objects.filter(user=user)

    return render(request, 'bookings.html', {'f_bookings': flight_bookings})


def search(request):
    # flight_obj = Flight.objects.all()
    # try:

    search = request.GET['from']
    search2 = request.GET['to']
    # search3 = request.GET['class']

    f_location = Flight.objects.filter(
        From__icontains=search, to__icontains=search2)

    # except:
    # return HttpResponse("Please Fill the details")

    context = {'search': f_location}
    return render(request, 'search.html', context=context)


def login_page(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user_obj = authenticate(username=username, password=password)
        if not user_obj:
            messages.error(request, "Please enter the correct details")
            return redirect('login')

        login(request, user_obj)
        messages.success(request, "You are logged in successfully!")
        return redirect('/')

    return render(request, 'login.html')


def register_page(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        user_obj = User.objects.filter(username=username, email=email)

        if user_obj.exists():
            messages.error(request, 'User already exists!')
            return redirect('register')

        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()
        messages.success(
            request, 'Your account has been created successfully!')
        return redirect('login')

    return render(request, 'register.html')


def handleLogout(request):
    logout(request)
    messages.success(request, 'Logout successfully!')
    return redirect('login')
