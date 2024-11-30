from rest_framework import serializers
from .models import ServiceRequest
from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

class UpdateServiceRequestStatusSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)

    class Meta:
        model = ServiceRequest
        fields = ['id', 'status', 'created_at', 'updated_at', 'resolved_at', 'email']
        read_only_fields = ['created_at', 'updated_at', 'resolved_at']

    def update(self, instance, validated_data):
        status = validated_data.get('status', instance.status)
        instance.status = status

        if status in ['resolved', 'completed', 'closed', 'cancelled'] and instance.resolved_at is None:
            instance.resolved_at = now()
        elif status not in ['resolved', 'completed', 'closed', 'cancelled']:
            instance.resolved_at = None

        instance.save()
        logger.info(f"ServiceRequest {instance.id} updated: status={instance.status}, resolved_at={instance.resolved_at}")
        return instance