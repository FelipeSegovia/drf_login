from django.shortcuts import render
from rest_framework import generics

from apis.user.models import User

from apis.user.serializer import UserSerializer


# Create your views here.
class UserList(generics.ListCreateAPIView):
    users = User.objects.all()
    serializer_class = UserSerializer
    