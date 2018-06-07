from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
import django_filters

from .models import Comments
from .serializers import CommentsSerializer

# Create your views here.
class CommentsViewset(viewsets.ModelViewSet):
    queryset = Comments.objects.all(),
    serializer_class = CommentsSerializer,