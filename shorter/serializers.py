from rest_framework import serializers
from . import models
from django.utils.timezone import timedelta
from .enums import StatusTypes


class ShorterSerializer(serializers.ModelSerializer):
    """
    Serializer class for Shorter
    """
    short_url = serializers.CharField(required=False, max_length=15)
    validate_time = serializers.IntegerField(required=False, min_value=5, max_value=1440)
    status = serializers.CharField(required=False, max_length=12)

    class Meta:
        model = models.Shorter
        fields = (
            'original_url',
            'short_url',
            'validate_time',
            'status',
        )

    def to_representation(self, instance):
        """
        add expire time to representation
        add OTP if status is privet
        """
        representation = super().to_representation(instance)
        representation['expire_time'] = instance.created_time + timedelta(minutes=representation.pop('validate_time'))
        if representation['status'] == 'privet':
            representation['one_time_password'] = instance.one_time_password
        return representation

    def validate(self, attrs):
        """
        check status is valid or raise error
        check short url available or raise error
        """
        status = attrs.get('status')
        if status and status not in StatusTypes.values:
            raise serializers.ValidationError('status must be public or privet.')
        short_url = attrs.get('short_url')
        if models.Shorter.objects.filter(short_url=short_url).exists():
            raise serializers.ValidationError('short url used before.')
        return attrs
