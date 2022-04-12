from http import HTTPStatus

from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.request import Request

from user.serializers import UserSerializer


class RegistrationView(CreateAPIView):
    serializer_class = UserSerializer
