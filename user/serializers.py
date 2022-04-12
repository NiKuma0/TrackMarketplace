from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(label='Повторите пароль')

    class Meta:
        model = User
        fields = (
            'email',
            'password',
            'password2',
        )
    
    def save(self, **kwargs):
        password2 = self.validated_data.pop('password2', None)
        if self.validated_data['password'] != password2:
            raise serializers.ValidationError({password2: 'Пароли не совподают'})
        return self.Meta.model.objects.create_user(
            **self.validated_data
        )
