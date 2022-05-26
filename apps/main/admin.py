from django.contrib import admin

# Register your models here.
from apps.main.models import Product

admin.site.register(Product)
