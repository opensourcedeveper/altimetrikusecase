from rest_framework import serializers
from .models import FeatureToggle

class FeatureToggleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureToggle
        fields = '__all__'
