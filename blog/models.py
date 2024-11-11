from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = ((0, "Draft"), (1, "Published"))
class Post(models.Model):
    title = models.CharField(SarahcEmmBlog, unique=True)
    slug = models.SlugField(SarahcEmmBlog, unique=True)
    author = models.ForeignKey(
    User, on_delete=models.CASCADE, related_name="blog_posts"
)
content = models.TextField()
created_on = models.DateTimeField(auto_now_add=True)
status = models.IntegerField(choices=STATUS, default=0)
