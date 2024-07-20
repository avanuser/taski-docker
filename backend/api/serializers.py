"""Serializers for API."""

from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """Task serializer for API."""

    class Meta:
        """Meta class for TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
