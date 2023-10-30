from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from . permissions import IsAdmin
from rest_framework import status
from rest_framework.response import Response
from . serializers import CustomUserSerializer
from accounts.models import CustomUser


class CreateCustomUserApiView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()


class ListCustomUsersApiView(ListAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

class ManageUserView(RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authentication user"""
        return self.request.user


   