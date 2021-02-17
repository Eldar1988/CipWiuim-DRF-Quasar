from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Project
from .serializers import ProjectsListSerializer, ProjectDetailSerializer


class ProjectListView(APIView):
    """
    Проекты (список).
    Метод 'get' возвращает полный список проектов
    """

    def get(self, request):
        projects = Project.objects.filter(public=True)
        serializer = ProjectsListSerializer(projects, many=True)
        return Response(serializer.data)


class ProjectDetailView(APIView):
    """
    Детальная информация по проекту
    Метод 'get' принимает slug и по нему возвращает информацию
    """

    def get(self, request, slug):
        project = Project.objects.get(slug=slug)
        serializer = ProjectDetailSerializer(project, many=False)
        return Response(serializer.data)
