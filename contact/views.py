from django.shortcuts import render
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView,ListAPIView
from .serializers import signupserializer, contactserializer
from rest_framework.response import Response
from rest_framework import status
from .models import contact
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.

class signupview(GenericAPIView):
    serializer_class = signupserializer

    def post(self, request, *args, **kwargs):
        serializer = signupserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class contactapiview(ListCreateAPIView):
    serializer_class = contactserializer
    permission_classes = [IsAuthenticatedOrReadOnly,]

    def get_queryset(self):
        return contact.objects.all()


class createcontactapiview(ListCreateAPIView):
    serializer_class = contactserializer
    permission_classes = [IsAuthenticatedOrReadOnly,]
    authentication_classes = [SessionAuthentication,]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return contact.objects.filter(owner=self.request.user)


class detailcontactapiview(RetrieveUpdateDestroyAPIView):
    serializer_class = contactserializer
    queryset = contact.objects.all()
    permission_classes =  [IsAuthenticatedOrReadOnly]
    lookup_field = 'id'
