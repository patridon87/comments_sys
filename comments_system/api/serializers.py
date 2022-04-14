from rest_framework import serializers
from comments.models import Post, Comment


class CommentInPostSerializer(serializers.ModelSerializer):
    replys = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('author', 'text', 'created', 'replys')

    def get_replys(self, obj):
        queryset = Comment.objects.filter(parent=obj, level__lte=3)
        serializer = CommentInPostSerializer(queryset, many=True)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replys = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('author', 'text', 'created', 'replys')

    def get_replys(self, obj):
        queryset = Comment.objects.filter(parent=obj)
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('author', 'text', 'comments')

    def get_comments(self, obj):
        queryset = Comment.objects.filter(post=obj, parent_id=None)
        serializer = CommentInPostSerializer(queryset, many=True)
        return serializer.data
