from rest_framework import serializers
from .models import MapPoint, Region, PointType


class MapPointsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = ('id', 'title', 'slug', 'coordinates')


class RegionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        exclude = ('order',)


class PointTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PointType
        exclude = ('order',)


class MapPointsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MapPoint
        fields = '__all__'
