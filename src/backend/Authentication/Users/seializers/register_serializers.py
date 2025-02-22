from rest_framework import serializers
from backend.Authentication.Users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=64, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric chars'
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ResendTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def create(self, validated_data):
        user = User.objects.get(email=validated_data['email'])

        return user


class VerifyEmailSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
# check it
