from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.filters import SearchFilter
import django_filters

from .models import Timeline
from. serializers import TimelineSerializer

# Create your views here.
class TimelineViewSet(viewsets.ModelViewSet):
    queryset = Timeline.objects.all()
    serializer_class = TimelineSerializer