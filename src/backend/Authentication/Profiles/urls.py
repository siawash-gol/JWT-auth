from .views.editprofile_views import EditProfileView, ChangePasswordView, SupportView
from .views.overview_views import OverView
from django.urls import path

urlpatterns = [
    path('overview', OverView.as_view(), name='overview'),
    path('<slug:slug>/edit-profile', EditProfileView.as_view(), name='edit_profile'),
    path('<slug:slug>/change-password', ChangePasswordView.as_view(), name='change_password'),
    path('<slug:slug>/support', SupportView.as_view(), name='support'),

]
