from django.contrib import admin

# -------------------------------------------------------------------
# django-admin login; username:admin password:market##7
# -------------------------------------------------------------------


# Register your models here.
from products.models import Product

admin.site.register(Product)
