from rest_framework import serializers
from .models import (
    Category,
    Blog,
    Comment,
    Like,
    PostView
)
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name'
        )


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    # post = serializers.StringRelatedField()

    class Meta:
        model = Comment
        fields = (
            'user',
            'content',
            'id',
            # 'time_stamp',
        )


class LikeSerializer(serializers.ModelSerializer):
    # author = serializers.StringRelatedField()
    # post = serializers.StringRelatedField()
    class Meta:
        model = Like
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()
    # category_id = serializers.IntegerField(write_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()
    post_views = serializers.SerializerMethodField()
    comment_count=serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'content',
            'image',
            'category',
            # 'category_id',
            'publish_date',
            'last_updated',
            'author',
            'status',
            'slug',
            'comments',
            'likes',
            'post_views',
            'comment_count'
        )

    def create(self, validated_data):
        author = User.objects.get(username=self.context['request'].user)
        validated_data['author'] = author
        return Blog.objects.create(**validated_data)
    
    def get_likes(self, obj):
        return list(Like.objects.filter(post=obj).values())

    def get_post_views(self, obj):
        return PostView.objects.filter(post=obj).count()
    
    def get_comment_count(self, obj):
        return Comment.objects.filter(post=obj).count()



# class PostVSerializer(serializers.ModelSerializer):
#     author = serializers.StringRelatedField()
#     post = serializers.StringRelatedField()

#     class Meta:
#         model = PostView
#         fields = (
#             'author',
#             'post',
#             'time_stamp'
#         )



  