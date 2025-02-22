from datetime import datetime
from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.Authentication.Profiles.models import Profile


class OverView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        profile = get_object_or_404(Profile, user=user)

        return Response({
            "Profile": {
                "username": profile.username,
                "email": profile.email,
                "first name": profile.first_name,
                "last name": profile.last_name,
                "language": profile.language,
                "phone": profile.phone,
                "state": profile.state,
                "city": profile.city,
            }
        }, status=status.HTTP_200_OK)
