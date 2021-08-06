from rest_framework import serializers
from django.contrib.auth.models import User
from .models import contact


class signupserializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=55, min_length=8, write_only=True)
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

    def validate(self, attrs):
        email = attrs.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exists')

        return attrs

    def create(self, validated_data):
        return User.objects.create(**validated_data)




class contactserializer(serializers.ModelSerializer):
    class Meta:
        model = contact
        fields = ['country_code', 'first_name', 'last_name', 'phone_number']
