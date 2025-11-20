from django.urls import path
from . import views

urlpatterns = [
    path('ocean/', views.ocean_data_dashboard, name='ocean_data_dashboard'),
]