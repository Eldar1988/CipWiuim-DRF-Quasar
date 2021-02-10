from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializers import ProjectsListSerializer, ProjectDetailSerializer


class ProjectListView(APIView):
    """Проекты (список)"""

    def get(self, request):
        projects = Project.objects.filter(public=True)
        serializer = ProjectsListSerializer(projects, many=True)
        return Response(serializer.data)
