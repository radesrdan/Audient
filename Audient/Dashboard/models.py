from django.db import models

# Create your models here.

class Post(models.Model):
    user_name = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class SubPosts(models.Model):
    question = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=20)
    post_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')