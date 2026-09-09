from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from . permissions import IsAdmin
from rest_framework import status
from rest_framework.response import Response
from . serializers import CustomUserSerializer, GallerySerializer, GalleryImageSerializer
from accounts.models import CustomUser
from gallery.models import Gallery, GalleryImage



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
    

class CreateGalleryApiView(CreateAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
    permission_classes = [IsAuthenticated]


class ListGalleryApiView(ListAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()


class RetrieveUpdateDestroyGalleryView(RetrieveUpdateDestroyAPIView):
    serializer_class = GallerySerializer
    queryset = Gallery.objects.all()
    permission_classes = [IsAuthenticated]
    lookup_field = 'id'


    def get(self, request, id):
        try:
            gallery = Gallery.objects.get(id=id)
            serializer = GallerySerializer(gallery)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Gallery.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class CreateGalleryImageApiView(CreateAPIView):
    serializer_class = GalleryImageSerializer
    queryset = GalleryImage.objects.all()
    permission_classes = [IsAuthenticated]


class ListGalleryImageApiView(ListAPIView):
    serializer_class = GallerySerializer
    queryset = GalleryImage.objects.all()



   