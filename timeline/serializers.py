from rest_framework import serializers

from .models import Timeline

# Serializers define the API representation.
class TimelineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Timeline
        fields = ('id', 'name', 'status', 'like' , 'pic')