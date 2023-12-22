from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

from apis.user.models import User
from apis.user.serializer import UserSerializer


# class UserAPI(APIView):
#
#     @staticmethod
#     def get_queryset(*args, **kwargs):
#         return User.objects.all()
#
#     @staticmethod
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#

@api_view(["GET"])
def get_users(request):
    user_model = User.objects.all()
    users = UserSerializer(user_model, many=True)
    return Response(users.data, status=status.HTTP_200_OK)


@api_view(["GET"])
def get_user_detail(request, pk: int):
    user_model = User.objects.filter(id=pk).first()
    if not user_model:
        return Response("Usuario no encontrado", status=status.HTTP_404_NOT_FOUND)
    else:
        user = UserSerializer(user_model)
        return Response(user.data, status=status.HTTP_200_OK)


@api_view(["POST"])
def create_user(request):
    new_user = UserSerializer(data=request.data)
    if new_user.is_valid():
        new_user.save()
        return Response(new_user.data, status=status.HTTP_201_CREATED)
    else:
        return Response(new_user.errors, status=status.HTTP_400_BAD_REQUEST)

