from rest_framework import serializers
from .models import Profile, Company


class ProfilesListSerializer(serializers.ModelSerializer):
    """Profiles list"""
    class Meta:
        model = Profile
        exclude = ('user', 'user_id', 'bio', 'public')


class CompanyListSerializer(serializers.ModelSerializer):
    """Companies list"""
    class Meta:
        model = Company
        exclude = ('')