from django.urls import path
from .api import get_users, get_user_detail

urlpatterns = [
    path('users/', get_users, name='users'),
    path('users/<int:pk>', get_user_detail, name='user_detail')
]
