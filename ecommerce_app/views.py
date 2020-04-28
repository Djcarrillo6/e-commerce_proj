from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import bcrypt


def index(request):
    return render(request, 'index.html')


def new_user(request):
    return render(request, 'newuser-regs.html')


def about_co(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def contact_co(request):
    return render(request, 'contact.html')


def shoppingcart(request):
    return render(request, 'shoppingcart.html')


def tinctures(request):
    return render(request, 'tinctures.html')


def capsules(request):
    return render(request, 'capsules.html')


def topicals(request):
    return render(request, 'topicals.html')


def community_wall(request):
    return render(request, 'wall.html')


def item_details(request):
    return render(request, 'item-details.html')


def register(request):
    errors = User.objects.validator(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    is_user_in_db = User.objects.filter(email=request.POST['email']).first()

    if is_user_in_db:
        print("Username already exists")
        return redirect("/")

    hashed_pw = bcrypt.hashpw(
        request.POST['password'].encode(), bcrypt.gensalt()).decode()

    user_created = User.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['lname'],
        email=request.POST['email'],
        password=hashed_pw
    )

    request.session['user_id'] = user_created.id

    return redirect("/")


def log(request):
    return render(request, 'logform.html')


def login(request):

    errors = User.objects.valid_login(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")

    found_user = User.objects.filter(email=request.POST['email']).first()

    if found_user:
        is_pw_correct = bcrypt.checkpw(
            request.POST['password'].encode(), found_user.password.encode())

        if is_pw_correct:
            request.session['user_id'] = found_user.id
            return redirect('/wishes')
        else:
            print("Password does NOT match our records!")
            return redirect("/")
    else:
        print("Email address does NOT match our records!")
        return redirect("/")


def logout(request):
    request.session.clear()
    return redirect("/")
