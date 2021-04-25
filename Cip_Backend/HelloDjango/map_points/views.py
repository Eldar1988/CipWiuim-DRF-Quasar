from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MapPoint, Region, PointType
from .serializers import MapPointsListSerializer, MapPointsDetailSerializer, RegionListSerializer, \
    PointTypeListSerializer


class MapPointsListView(APIView):
    """Список объектов на карте"""
    def get(self, reguest, region, point_type=None):
        response_data = {}

        if point_type == 'None':
            points = MapPoint.objects.filter(region__slug=region)
        else:
            points = MapPoint.objects.filter(region__slug=region, type__slug=point_type)

        serializer = MapPointsListSerializer(points, many=True)
        response_data['points'] = serializer.data

        region = Region.objects.get(slug=region)
        region_serializer = RegionListSerializer(region, many=False)
        response_data['region'] = region_serializer.data

        return Response(response_data)


class RegionsListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class PointTypesListView(generics.ListAPIView):
    queryset = PointType.objects.all()
    serializer_class = PointTypeListSerializer


class MapPointDetailView(APIView):

    def get(self, request, slug):
        point = MapPoint.objects.get(slug=slug)
        serializer = MapPointsDetailSerializer(point, many=False)
        return Response(serializer.data)