from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import login_page, register_page, guest_register_view
from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_page, name='contact'),
    path('login', login_page, name='login'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', register_page, name='register'),
]
