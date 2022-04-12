from rest_framework.generics import CreateAPIView

from user.serializers import UserSerializer


class RegistrationView(CreateAPIView):
    serializer_class = UserSerializer
