from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MapPoint, Region, PointType
from .serializers import MapPointsListSerializer, MapPointsDetailSerializer, RegionListSerializer, \
    PointTypeListSerializer


class MapPointsListView(APIView):
    """Список объектов на карте"""
    def get(self, reguest, region=None, point_type=None):

        if point_type == 'None':
            points = MapPoint.objects.filter(region__slug=region)
        else:
            points = MapPoint.objects.filter(region__slug=region, type__slug=point_type)

        serializer = MapPointsListSerializer(points, many=True)
        return Response(serializer.data)


class RegionsListView(generics.ListAPIView):
    queryset = Region.objects.all()
    serializer_class = RegionListSerializer


class PointTypesListView(generics.ListAPIView):
    queryset = PointType.objects.all()
    serializer_class = PointTypeListSerializer
