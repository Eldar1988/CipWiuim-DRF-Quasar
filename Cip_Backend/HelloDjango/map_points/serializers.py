from rest_framework import serializers
from .models import MapPoint, Region, PointType


class MapPointsListSerializer(serializers.ModelSerializer):
    type = serializers.SlugRelatedField(slug_field='title', many=True, read_only=True)

    class Meta:
        model = MapPoint
        fields = ('id', 'title', 'slug', 'coordinates', 'type')


class PointsForRegion(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = ('id',)


class RegionListSerializer(serializers.ModelSerializer):
    points = PointsForRegion(many=True, read_only=True)

    class Meta:
        model = Region
        exclude = ('order',)


class PointTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointType
        exclude = ('order',)


class MapPointsDetailSerializer(serializers.ModelSerializer):
    region = RegionListSerializer(many=False, read_only=True)

    class Meta:
        model = MapPoint
        fields = '__all__'
