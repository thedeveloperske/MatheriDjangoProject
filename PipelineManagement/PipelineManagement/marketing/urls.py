from django.urls import path
from . import views

urlpatterns = [
    path('marketing', views.submit_form, name='submit_form')
]
