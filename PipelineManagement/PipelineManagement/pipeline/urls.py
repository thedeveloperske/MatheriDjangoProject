from django.urls import path
from . import views

urlpatterns = [
    path('pipeline', views.submit_pipeline, name='submit_pipeline')
]
