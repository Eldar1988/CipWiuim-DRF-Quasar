from rest_framework.views import APIView
from rest_framework.response import Response

from .models import CallBack
from .serializers import CallBackSerializer


class CallBackCreateView(APIView):
    def post(self, request):
        serializer = CallBackSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(status=400)
