from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from services import views as services_views  # Correct aliasing

urlpatterns = [
    path('', views.index, name='shop'),  # Main shop homepage
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('login/', auth_views.LoginView.as_view(template_name='shop/login.html'), name='login'),  # Login page
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout action
    path('register/', views.register, name='register'),  # Registration page
    path('contact/', services_views.contact_view, name='contact'),  # Correct usage of services_views
]

