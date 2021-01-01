from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post
from .serializers import PostsListSerializer


class FuturePostsListView(APIView):
    """Posts list"""
    def get(self, request):
        posts = Post.objects.filter(public=True, future=True)
        serializer = PostsListSerializer(posts, many=True)
        return Response(serializer.data)

