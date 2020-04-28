from django.urls import path
from . import views

# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    path('new-registration', views.new_user),
    path('login', views.log),
    path('about', views.about_co),
    path('product1', views.item_details),
    path('services', views.services),
    path('contact', views.contact_co),
    path('shoppingcart', views.shoppingcart),
    path('products/tinctures', views.tinctures),
    path('products/capsules', views.capsules),
    path('products/topicals', views.topicals),
    path('community', views.community_wall),

]
