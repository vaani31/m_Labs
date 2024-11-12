from django.urls import path
from . import views

urlpatterns = [
    path('htop/', views.htop_view, name='htop')
]
