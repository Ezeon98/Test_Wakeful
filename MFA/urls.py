from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='usuarios'),
]