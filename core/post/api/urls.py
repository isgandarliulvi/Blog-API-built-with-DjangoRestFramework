from django.urls import path
from post.api import views as api_views

urlpatterns = [
    path('posts/', api_views.PostListCreateAPIView.as_view(), name = "posts-list"),
    path('posts/<int:pk>/', api_views.PostDetailAPIView.as_view(), name = "posts-detail"),
    path('posts/<int:post_pk>/write-comment/', api_views.CommentCreateAPIView.as_view(), name = "post-comment"),
    path('comments/<int:pk>/', api_views.CommentDetailAPIView.as_view(), name = "comments"),
    path('profile/', api_views.ProfileListCreateAPIView.as_view(), name = "profiles-list"),
    path('profile/<int:pk>/', api_views.ProfileDetailAPIView.as_view(), name = "profiles-detail"),
    path('category/', api_views.CategoryListCreateAPIView.as_view(), name = "category-list"),
    path('category/<int:pk>/', api_views.CategoryDetailAPIView.as_view(), name = "category-detail"),

]




