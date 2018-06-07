from rest_framework import serializers

from .models import Comments

# Serializers define the API representation.
class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('id', 'name', 'comment', 'timeline')