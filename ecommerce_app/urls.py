from django.urls import path
from django.contrib.auth.views import LogoutView
from accounts.views import LoginView, RegisterView, guest_register_view
from addresses.views import checkout_address_create_view, checkout_address_reuse_view
from billing.views import payment_method_view, payment_method_createview
from carts.views import cart_detail_api_view

from . import views


# NO LEADING SLASHES
urlpatterns = [
    path('', views.home_page, name='home'),
    path('about', views.about_page, name='about'),
    path('contact', views.contact_page, name='contact'),
    path('login', LoginView.as_view(), name='login'),
    path('checkout/address/create/', checkout_address_create_view,
         name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view,
         name='checkout_address_reuse'),
    path('register/guest/', guest_register_view, name='guest_register'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('register', RegisterView.as_view(), name='register'),
    path('billing/payment-method', payment_method_view,
         name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_createview,
         name='billing-payment-method-endpoint'),
]
