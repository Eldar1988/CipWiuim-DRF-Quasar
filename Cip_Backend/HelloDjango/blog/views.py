from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post, Comment
from .serializers import PostsListSerializer, PostDetailSerializer, CommentsSerializer


class FuturePostsListView(APIView):
    """Future Posts list"""
    def get(self, request):
        posts = Post.objects.filter(public=True, future=True)
        serializer = PostsListSerializer(posts, many=True)
        return Response(serializer.data)


class PostsListView(APIView):
    """Posts list"""
    def get(self, request):
        posts = Post.objects.filter(public=True)
        serializer = PostsListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):
    """Post detail"""
    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        serializer = PostDetailSerializer(post, many=False)
        post.views += 1
        post.save()
        return Response(serializer.data)


class CreateCommentView(APIView):
    """Create comment"""
    def post(self, requset):
        serializer = CommentsSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201)

        return Response(status=500)
