from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import login_page, register_page, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_page, name='contact'),
    path('login', login_page, name='login'),
    path('checkout/address/create/', checkout_address_create_view,
         name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view,
         name='checkout_address_reuse'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('register', register_page, name='register'),
]
