from rest_framework import serializers
from .models import Contact, SocialNetwork


class ContactsSerializer(serializers.ModelSerializer):
    """Cipwiuim contacts"""
    class Meta:
        model = Contact
        fields = '__all__'


class SocialNetworksSerializer(serializers.ModelSerializer):
    """Social networks serializer"""
    class Meta:
        model = SocialNetwork
        fields = '__all__'
