from django.urls import path
from . import views

urlpatterns = [
    path('', views.services_view, name='services'),
    path('design-service/', views.design_service_view, name='design_service'),
    path('logo-design/', views.logo_design_view, name='logo_design'),
    path('poster-design/', views.poster_design_view, name='poster_design'),
    path('social-media-design/', views.social_media_design_view, name='social_media_design'),
    path('contact/', views.contact_view, name='contact'),
]
