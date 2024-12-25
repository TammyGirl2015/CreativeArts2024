from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='shop_home'),
    path('checkout/', views.checkout, name='checkout'),
]
