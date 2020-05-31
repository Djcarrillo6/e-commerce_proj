from django.contrib.auth import authenticate, login, get_user_model

from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from .models import *
from django.contrib import messages
from .forms import *


# def index(request):
# return render(request, 'products/list.html')


def home_page(request):
    context = {
        "title": "Home Page",
        "content": "Welcome to My Ecommerce Home Page"
    }
    # if user is authen, pass specific user dictionary
    if request.user.is_authenticated:
        context["premium_content"] = "Premo Cont Coming.."
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": "All About This Ecommerce Store"
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    # to instantiate this form class
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact Page",
        "content": "Information to Contact Us",
        "form": contact_form,
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
        if request.is_ajax():
            return JsonResponse({"message": "Thank you for your submission"})

    if contact_form.errors:
        errors = contact_form.errors.as_json()
        if request.is_ajax():
            return HttpResponse(errors, status=400, content_type='application/json')

    return render(request, "contact/view.html", context)
