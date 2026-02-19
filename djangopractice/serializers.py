from rest_framework import serializers
from .models import User


# <Name of model>Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'uuid',
            'first_name',
            'middle_name',
            'last_name',
            'email',
            'mobile_number',
            'date_of_birth',
            'gender',
            'address'
        ]