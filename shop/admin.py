from django.contrib import admin
from .models import CustomUser, Order

admin.site.register(CustomUser)
admin.site.register(Order)
