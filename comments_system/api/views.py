from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from comments.models import Post, Comment
from .serializers import (PostSerializer, CommentSerializer,
                          CommentInPostSerializer)


class CreateRetrievePostViewSet(viewsets.GenericViewSet,
                                mixins.CreateModelMixin,
                                mixins.RetrieveModelMixin):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CreateListCommentViewSet(viewsets.GenericViewSet,
                               mixins.CreateModelMixin,
                               ):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CommentInPostSerializer
        return CommentSerializer

    def perform_create(self, serializer):
        post_id = self.kwargs.get("post_id")
        parent_id = self.request.data.get("parent_id", None)
        post = get_object_or_404(Post, pk=post_id)
        if parent_id:
            parent = get_object_or_404(Comment, pk=parent_id)
            serializer.save(post=post, parent=parent, level=parent.level + 1)
        else:
            serializer.save(post=post)


class RertrieveCommentVewSet(viewsets.GenericViewSet,
                             mixins.RetrieveModelMixin):
    queryset = Comment.objects.filter(level=3)
    serializer_class = CommentSerializer
