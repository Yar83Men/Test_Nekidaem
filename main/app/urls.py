from django.urls import path

from .views import PostsView, UsersView, UserPostsView

urlpatterns = [
    path('posts/', PostsView.as_view(), name="all_posts"),
    path('users/', UsersView.as_view(), name="all_users"),
    path('user/<int:user_id>', UserPostsView.as_view(), name="user_posts")
]