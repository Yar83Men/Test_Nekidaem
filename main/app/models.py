from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    blog_subscribed = models.ManyToManyField('Blog', blank=True)
    post_read = models.ManyToManyField('Posts', blank=True)


    def __str__(self):
        return self.user.username

class Blog(models.Model):
    blog_name = models.CharField(max_length=150)
    user_blog = models.OneToOneField('Users', on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_name



class Posts(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Lenta(models.Model):
    blog = models.ManyToManyField(Blog)
    user = models.OneToOneField(Users, on_delete=models.CASCADE)

    def __str__(self):
        return f'Лента {self.user.username}'


