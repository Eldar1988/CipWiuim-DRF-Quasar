from rest_framework import serializers
from .models import Project, DigitalIndicator, Benefit, Structure, QuestionAndAnswer, Review, ProjectVideo, ProjectFile, ProjectPhoto
from companies.serializers import CompanyForProjectsSerializer
from forum.models import Theme


class ProjectsListSerializer(serializers.ModelSerializer):
    """Projects list"""
    class Meta:
        model = Project
        exclude = ('project_admin', 'short_description', 'bio', 'order', 'public', 'pub_date', 'update', 'views')


class DigitalIndicatorsSerializer(serializers.ModelSerializer):
    """Project digital indicators"""
    class Meta:
        model = DigitalIndicator
        exclude = ('pub_date', 'update', 'order', 'project')


class BenefitsSerializer(serializers.ModelSerializer):
    """Project benefits"""
    class Meta:
        model = Benefit
        exclude = ('pub_date', 'update', 'order', 'project')


class StructuresListSerializer(serializers.ModelSerializer):
    """Project structures list serializer"""
    class Meta:
        model = Structure
        exclude = ('project', 'seo_description', 'image', 'order', 'public', 'pub_date', 'update')


class QuestionsAndAnswersSerializer(serializers.ModelSerializer):
    """Project questions and answers"""
    class Meta:
        model = QuestionAndAnswer
        exclude = ('project', 'order', 'pub_date', 'update')


class ReviewsSerializer(serializers.ModelSerializer):
    """Project reviews"""
    class Meta:
        model = Review
        exclude = ('project', 'order', 'public', 'pub_date', 'update')


class ProjectVideosSerializer(serializers.ModelSerializer):
    """Project videos"""
    class Meta:
        model = ProjectVideo
        exclude = ('project', 'order', 'pub_date', 'update')


class ProjectPhotosSerializer(serializers.ModelSerializer):
    """Project photos"""
    class Meta:
        model = ProjectPhoto
        exclude = ('project', 'order', 'pub_date', 'update')


class ProjectFilesSerializer(serializers.ModelSerializer):
    """Project photos"""
    class Meta:
        model = ProjectFile
        exclude = ('project', 'order', 'pub_date', 'update')


class ForumThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Theme
        fields = ('slug',)


class ProjectDetailSerializer(serializers.ModelSerializer):
    """Project detail"""
    indicators = DigitalIndicatorsSerializer(many=True)
    benefits = BenefitsSerializer(many=True)
    structures = StructuresListSerializer(many=True)
    questions = QuestionsAndAnswersSerializer(many=True)
    reviews = ReviewsSerializer(many=True)
    videos = ProjectVideosSerializer(many=True)
    photos = ProjectPhotosSerializer(many=True)
    files = ProjectFilesSerializer(many=True)
    company = CompanyForProjectsSerializer(many=False)
    forum_themes = ForumThemeSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        exclude = ('project_admin', 'order', 'slug', 'public', 'pub_date', 'update', 'views')


class StructureDetailSerializer(serializers.ModelSerializer):
    """Project structure serializer"""
    class Meta:
        model = Structure
        exclude = ('project', 'order', 'pub_date', 'public', 'update')

