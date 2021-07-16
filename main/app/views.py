from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Users, Blog, Posts


class PostsView(ListView):
    model = Posts
    template_name = 'app/all_posts.html'
    context_object_name = 'posts'



class UsersView(ListView):
    model = Users
    template_name = 'app/all_users.html'
    context_object_name = 'users'

class UserPostsView(DetailView):
    model = Users
    template_name = 'app/user_posts.html'
    context_object_name = 'users'
    pk_url_kwarg = 'user_id'

