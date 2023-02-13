from rest_framework import serializers

from users.models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email',
                   'photo', 'phone_number', 'address', 'date_joined')
    