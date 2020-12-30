from rest_framework import serializers
from .models import Theme, Answer
from companies.serializers import ProfilesListSerializer
from companies.serializers import ProfilesListSerializer


class ThemesListSerializer(serializers.ModelSerializer):
    """Themes list"""
    author = ProfilesListSerializer(many=False)

    class Meta:
        model = Theme
        exclude = ('pub_date', 'body', 'update', 'order')


class AnswersSerializer(serializers.ModelSerializer):
    """Theme answers"""

    class Meta:
        model = Answer
        exclude = ('public',)


class ThemeDetailSerializer(serializers.ModelSerializer):
    """Forum theme detail"""
    answers = AnswersSerializer(many=True)

    class Meta:
        model = Theme
        exclude = ('pub_date', 'update')