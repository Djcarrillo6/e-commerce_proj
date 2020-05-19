from django.urls import path
from . import views
from products.views import (
    ProductListView,
    product_list_view,
    ProductDetailView,
    product_detail_view,
    ProductFeaturedListView,
    ProductFeaturedDetailView
)


# NO LEADING SLASHES
urlpatterns = [
    path('', views.index, name='index'),
    # path('new-registration', views.log),
    # path('register', views.register),
    # path('login', views.log),
    # path('logout', views.logout),
    # path('user-login', views.login),
    # path('about', views.about_co),
    # path('product1', views.item_details),
    # path('services', views.services),
    # path('contact', views.contact_co),
    # path('shoppingcart', views.shoppingcart),
    # path('products/tinctures', views.tinctures),
    # path('products/capsules', views.capsules),
    # path('products/topicals', views.topicals),
    # path('community', views.community_wall),

    # Newly added routes from (CFE-05/16)
    path('featured/', ProductFeaturedListView.as_view()),
    path('featured/<int:pk>', ProductFeaturedDetailView.as_view()),
    path('products', ProductListView.as_view()),  # class based view
    path('products-fbv', product_list_view),  # function based view
    path('products/<int:pk>', ProductDetailView.as_view()),  # class based view
    path('products-fbv/<int:pk>', product_detail_view),  # function based view


]
