from rest_framework import serializers
from .models import Post, Comment, PostLikes



class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'auther_id', 'title', 'content', 'publish_date', 'comments', 'slug', 'likes_count', 'comments_count' ]


    def get_likes_count(self, object):
        return PostLikes.objects.filter(post=object).count()

    

    def get_comments_count(self, object):
        return Comment.objects.filter(post=object).count()



class PostLikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLikes
        fields = '__all__'