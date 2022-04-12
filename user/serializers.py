from rest_framework import serializers
from rest_framework_simplejwt.serializers import PasswordField

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password = PasswordField(label='Пароль')
    password2 = PasswordField(label='Повторите пароль')

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2',
        )
    
    def save(self, **kwargs):
        validated_data = {**self.validated_data, **kwargs}
        password2 = validated_data.pop('password2', None)
        if validated_data['password'] != password2:
            raise serializers.ValidationError({password2: 'Пароли не совподают'})
        return self.Meta.model.objects.create_user(
            **validated_data
        )
