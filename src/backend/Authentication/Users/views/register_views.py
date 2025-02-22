from ..seializers.register_serializers import RegisterSerializer, VerifyEmailSerializer, ResendTokenSerializer
from django.contrib.sites.shortcuts import get_current_site
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status, views
from backend.Authentication.Profiles.models import Profile
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from datetime import datetime, timedelta
from ..renderers import UserRenderer
from django.conf import settings
from django.urls import reverse
from drf_yasg import openapi
from ..models import User
from ..utils import Util
import jwt


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    renderer_classes = (UserRenderer,)

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        user_data = serializer.data
        user = User.objects.get(email=user_data['email'])
        token = RefreshToken.for_user(user).access_token
        current_site = get_current_site(request).domain
        relative_link = reverse('email_verify')
        abstract_link = 'http://' + current_site + relative_link + "?token=" + str(token)
        email_body = 'Hi' + user.username + ' to complete registration click on the link\n' + abstract_link
        data = {'email_body': email_body, 'email_to': user.email, 'email_subject': 'verify your email'}
        # Util.send_email(data)
        return Response({
            "message": "We have sent verify token to your email",
            "data": user_data
        }, status=status.HTTP_201_CREATED)


class ResendTokenVerifyEmailView(generics.GenericAPIView):
    serializer_class = ResendTokenSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']

        try:
            user = User.objects.get(email=email)
            if user.verified_email:
                return Response({"message": "your email is already verified"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken.for_user(user).access_token
            current_site = get_current_site(request).domain
            relative_link = reverse('email_verify')
            abstract_link = 'http://' + current_site + relative_link + "?token=" + str(token)
            email_body = 'hello my friend ' + user.username + ' we have resent token click on the link\n' + abstract_link
            data = {'email_body': email_body, 'email_to': user.email, 'email_subject': 'verify your email'}
            # Util.send_email(data)
            return Response({
                "message": "We have resent verify token to your email",
                "data": email
            }, status=status.HTTP_201_CREATED)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=status.HTTP_400_BAD_REQUEST)


class VerifyEmailView(views.APIView):
    serializer_class = VerifyEmailSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        token = request.GET.get('token')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            user = User.objects.get(id=payload['user_id'])
            if not user.verified_email:
                user.verified_email = True
                user.save()
                Profile.objects.create(
                    user=user,
                    email=user.email,
                    username=user.username,
                )
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)
        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation Expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

