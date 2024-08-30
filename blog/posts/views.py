from rest_framework import generics , status
from rest_framework.response import Response

from .models import Post, PostLikes, Comment
from .serializers import PostSerializer, PostLikesSerializer, CommentSerializer



class PostListAPI(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetailAPI(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateCommetAPI(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class PostLikesAPI(generics.CreateAPIView):
    queryset = PostLikes.objects.all()
    serializer_class = PostLikesSerializer    
