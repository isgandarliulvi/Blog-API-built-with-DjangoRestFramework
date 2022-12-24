from rest_framework import serializers
from post.models import Post, Category, Comment, Profile


class CommentSerializer(serializers.ModelSerializer):
    commenter = serializers.StringRelatedField(read_only = True)

    class Meta:
        model = Comment
        exclude = ["post"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many = True, read_only = True)

    class Meta:
        model = Post
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    posts = PostSerializer(many = True)
    class Meta:
        model = Category
        fields = "__all__"


class ProfileSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name = "post-detail",
    )

    class Meta:
        model = Profile
        fields = "__all__"