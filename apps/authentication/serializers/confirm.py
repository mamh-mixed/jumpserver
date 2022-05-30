from rest_framework import serializers

from common.drf.fields import EncryptedField
from ..const import ConfirmType


class ConfirmSerializer(serializers.Serializer):
    confirm_type = serializers.CharField(
        required=True, choices=ConfirmType.choices, max_length=64
    )
    secret_key = EncryptedField()
