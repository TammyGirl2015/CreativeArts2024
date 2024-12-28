"""creative_arts_2024 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from shop import views as shop_views  # Import views from shop
from services import views as services_views  # Import views from services

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', shop_views.home, name='home'),  # Use the correct import for home view
    path('shop/', include('shop.urls')),
    path('services/', include('services.urls')),
    path('contact/', services_views.contact_view, name='contact'),  # Correctly reference the contact view
]



