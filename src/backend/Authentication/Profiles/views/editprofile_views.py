from ..serializers.editprofile_serializers import EditProfileSerializer, ChangePasswordSerializer
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from backend.Authentication.Users.models import User
from rest_framework import generics
from ..models import Profile, Contact
from ..serializers.editprofile_serializers import SupportSerializer


class EditProfileView(RetrieveUpdateAPIView):
    serializer_class = EditProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user.profile


class ChangePasswordView(generics.UpdateAPIView):
    queryset = User.objects.all()
    lookup_field = 'slug'
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


class SupportView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = SupportSerializer
