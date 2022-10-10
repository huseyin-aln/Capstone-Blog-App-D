from rest_framework import serializers
from .models import (
    Category,
    Post,
    Comment,
    Like,
    PostV
)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'category',
            'category_id',
            'publish_date',
            'last_updated',
            'author',
            'status',
            'slug'
        )


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'author',
            'post',
            'time_stamp',
            'content'
        )


class LikeSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = Like
        fields = (
            'author',
            'post',
        )


class PostVSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    post = serializers.StringRelatedField()

    class Meta:
        model = PostV
        fields = (
            'author',
            'post',
            'time_stamp'
        )



  