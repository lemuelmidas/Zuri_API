from django.shortcuts import render

# Create your views here.


#import local viewsets
from rest_framework import viewsets

#import local data
from .serializers import LinkSerializer
from .models import Links


#create a viewset
class PostListApi(viewsets.ListAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostCreateApi(viewsets.CreateAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostDetailApi(viewsets.RetrieveAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostUpdateApi(viewsets.UpdateAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

#create another viewset
class PostDeleteApi(viewsets.DestroyAPIView):
    #define queryset
    queryset= Links.objects.filter(active=True)

    #specify serializer to be used
    serializer_class= LinkSerializer

