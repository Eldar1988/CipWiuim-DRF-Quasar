from rest_framework import serializers
from .models import Theme, Answer
from companies.serializers import ProfilesListSerializer
from companies.serializers import ProfilesListSerializer
from projects.serializers import ProjectsListSerializer


class AnswersChildSerializer(serializers.ModelSerializer):
    """Theme answers"""

    class Meta:
        model = Answer
        exclude = ('public',)


class AnswersSerializer(serializers.ModelSerializer):
    """Theme answers"""
    answer_for = AnswersChildSerializer(many=False)

    class Meta:
        model = Answer
        exclude = ('public',)


class AnswersIdsSerializer(serializers.ModelSerializer):
    """Theme answers"""

    class Meta:
        model = Answer
        fields = ('id',)


class ThemesListSerializer(serializers.ModelSerializer):
    """Themes list"""
    author = ProfilesListSerializer(many=False)
    project = ProjectsListSerializer(many=False)
    answers = AnswersIdsSerializer(many=True)

    class Meta:
        model = Theme
        exclude = ('body', 'update', 'order')


class ThemeDetailSerializer(serializers.ModelSerializer):
    """Forum theme detail"""
    author = ProfilesListSerializer(many=False)
    answers = AnswersSerializer(many=True)
    project = ProjectsListSerializer(many=False)

    class Meta:
        model = Theme
        exclude = ('update',)


class CreateAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
