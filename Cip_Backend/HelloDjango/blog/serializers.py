from rest_framework import serializers
from .models import Category, Post, Comment, PostPhoto


class PostsListSerializer(serializers.ModelSerializer):
    """Posts list"""
    category = serializers.SlugRelatedField(slug_field='title', read_only=True)

    class Meta:
        model = Post
        exclude = ('body', 'future', 'public', 'order', 'update')


class CategoriesSerializer(serializers.ModelSerializer):
    """Post categories"""
    class Meta:
        model = Category
        exclude = ('order',)


class CommentsSerializer(serializers.ModelSerializer):
    """Post comments"""
    class Meta:
        model = Comment
        exclude = ('public',)


class PostPhotosSerializer(serializers.ModelSerializer):
    """Post photos"""
    class Meta:
        model = PostPhoto
        exclude = ('post', 'order', 'pub_date', 'update')


class PostDetailSerializer(serializers.ModelSerializer):
    """Post detail"""
    comments = CommentsSerializer(many=True)
    images = PostPhotosSerializer(many=True)

    class Meta:
        model = Post
        exclude = ('public', 'future', 'order', 'update')
