from rest_framework import viewsets
# from django.contrib.auth.decorators import login_required
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostV
)
from .serializers import (
    CategorySerializer,
    CommentSerializer,
    PostSerializer,
    LikeSerializer,
    PostVSerializer
)


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class PostVView(viewsets.ModelViewSet):
    queryset = PostV.objects.all()
    serializer_class = PostVSerializer