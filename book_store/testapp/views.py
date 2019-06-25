from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Book
from .serializers import BookSerializers
from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .permissions import ChandanPermission
# Create your views here.

class BookView(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    authentication_classes = [TokenAuthentication,]
    permission_classes = [ChandanPermission,]
