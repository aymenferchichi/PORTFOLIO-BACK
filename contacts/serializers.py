from rest_framework import serializers

from .models import ContactMessage


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = [
            'id',
            'name',
            'email',
            'subject',
            'phone',
            'message',
            'estimator_project_type',
            'estimator_page_scope',
            'estimator_timeline',
            'estimator_support_level',
            'estimator_budget_min',
            'estimator_budget_max',
            'status',
            'created_at',
            'updated_at',
        ]
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']