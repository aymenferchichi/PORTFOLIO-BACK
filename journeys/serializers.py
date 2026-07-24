from rest_framework import serializers

from .models import Journey


class JourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = Journey
        fields = [
            'id',
            'slug',
            'year',
            'title',
            'eyebrow',
            'detail',
            'summary',
            'focus',
            'accent',
            'display_order',
        ]
        read_only_fields = fields
