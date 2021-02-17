from rest_framework import serializers
from .models import Profile, Company


class ProfilesListSerializer(serializers.ModelSerializer):
    """Profiles list"""
    class Meta:
        model = Profile
        exclude = ('user', 'uID', 'bio', 'public')


class CompanyListSerializer(serializers.ModelSerializer):
    """Companies list"""
    class Meta:
        model = Company
        exclude = ('admin_profile', 'bio', 'requisites', 'address', 'phone', 'cooperators', 'public', 'register_date')


class ProfileDetailSerializer(serializers.ModelSerializer):
    """User profile detail"""
    """Profiles list"""

    class Meta:
        model = Profile
        exclude = ('user', 'uID', 'public')


class CompanyDetailSerializer(serializers.ModelSerializer):
    """Company detail"""
    cooperators = ProfilesListSerializer(many=True)

    class Meta:
        model = Company
        exclude = ('admin_profile', 'public', 'register_date')


class CompanyForProjectsSerializer(serializers.ModelSerializer):
    """Сериализатор компании для деталей проекта"""
    cooperators = ProfilesListSerializer(many=True)

    class Meta:
        model = Company
        exclude = ('admin_profile', 'public', 'register_date', 'bio', 'address', 'requisites')
