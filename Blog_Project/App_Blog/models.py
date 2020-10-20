from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'post_author')
    blog_title = models.CharField(max_length=300, verbose_name='Pur your Title')
    slug = models.SlugField(max_length=300, unique=True)
    blog_content = models.TextField(verbose_name="Let's start a Blog: ")
    blog_image = models.ImageField(upload_to='blog_images', verbose_name='Image Here')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ['-publish_date']



    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='blog_comment')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-comment_date"]


    def __str__(self):
        return self.comment


class Likes(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='liked_blog')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='liker_user')


    def __str__(self):
        return self.user+ ' likes ' +self.blog
