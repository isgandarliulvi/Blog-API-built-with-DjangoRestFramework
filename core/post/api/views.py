from rest_framework import generics
from rest_framework.generics import get_object_or_404

from post.api.serializers import PostSerializer, CommentSerializer, CategorySerializer, ProfileSerializer
from post.models import Post, Category, Comment, Profile
from rest_framework import permissions
from post.api.permissions import IsAdminOrReadOnly, IsCommenterOrReadOnly
from rest_framework.exceptions import ValidationError


class PostListCreateAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

class PostDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAdminOrReadOnly]

class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        post_pk = self.kwargs.get("post_pk")
        post = get_object_or_404(Post, pk = post_pk)
        user = self.request.user
        comments = Comment.objects.filter(post = post, commenter = user)
        if comments.exists():
            raise ValidationError("You can add only one comment for one post.")
        serializer.save(post = post, commenter = user)

class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_class = [IsCommenterOrReadOnly]

class ProfileListCreateAPIView(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class CategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]


