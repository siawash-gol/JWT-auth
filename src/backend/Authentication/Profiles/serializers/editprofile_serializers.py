from rest_framework import serializers
from backend.Authentication.Users.models import User
from backend.Authentication.Profiles.models import Contact, Profile


class EditProfileSerializer(serializers.ModelSerializer):
    state = serializers.CharField(read_only=True)
    class Meta:
        model = Profile
        fields = ['username', 'email', 'first_name', 'last_name', 'language', 'phone', 'state', 'city']


class ChangePasswordSerializer(serializers.ModelSerializer):
    current_password = serializers.CharField(write_only=True, required=True)
    new_password = serializers.CharField(write_only=True)
    enter_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['current_password', 'new_password', 'enter_password']

    def validate(self, attrs):
        if attrs['new_password'] != attrs['enter_password']:
            raise serializers.ValidationError({"password": "Passwords must be match"})
        return attrs

    def validate_current_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"current_password": "Your current password is wrong!"})
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data['new_password'])
        instance.save()
        return instance


class SupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['email', 'full_name', 'message']

    def validate_email(self, value):
        user_email = self.context['request'].user.email
        if value != user_email:
            raise serializers.ValidationError({"email_error": "Your email address is wrong"})
        return value
