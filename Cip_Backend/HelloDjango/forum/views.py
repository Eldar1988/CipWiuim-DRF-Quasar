from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import ThemesListSerializer, ThemeDetailSerializer, AnswersSerializer, CreateAnswerSerializer
from .models import Theme, Answer


class ThemesListView(APIView):
    """
    Метод 'get' возвращает список тем форума
    """

    def get(self, request):
        themes = Theme.objects.filter(public=True)
        serializer = ThemesListSerializer(themes, many=True)
        return Response(serializer.data)


class ThemeDetailView(APIView):
    """
    Метод 'get' возращает тему форума по полю 'slug'
    """

    def get(self, request, slug):
        theme = Theme.objects.get(slug=slug)
        serializer = ThemeDetailSerializer(theme, many=False)
        return Response(serializer.data)


class CreateAnswerView(APIView):
    """
    Метод 'post' принимает данные нового сообщения и сохраняет в базу (+ Отправка в телеграм)
    """

    def post(self, request):
        serializer = CreateAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(status=500)
