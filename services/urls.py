from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_view, name='services'),
    path('design-service/', views.design_service_view, name='design_service'),
]
