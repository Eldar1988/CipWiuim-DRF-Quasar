from rest_framework import serializers
from .models import Theme, Answer


class ThemesListSerializer(serializers.ModelSerializer):
    """Themes list"""
    class Meta:
        model = Theme
        exclude = ('')