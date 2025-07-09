from rest_framework import serializers
from .models import FormData

class FormDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormData
        fields = ['id', 'name', 'email', 'message', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']