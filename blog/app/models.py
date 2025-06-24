from django.db import models
import uuid
from django.contrib.auth.models import User
class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.category_name
class Blog(models.Model):
    blog_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    blog_writer = models.ForeignKey(User,on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=150)
    blog_body = models.CharField(max_length=7500)
    blog_categories = models.ManyToManyField(Category,related_name='blogs')
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    def __str__(self):
        return self.blog_title
class Reviews(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    review_writer = models.ForeignKey(User,on_delete=models.CASCADE)
    review_title = models.CharField(max_length=150)
    review_body = models.CharField(max_length=1500)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    for_blog = models.ForeignKey(Blog,related_name='reviews',on_delete=models.CASCADE)
    def __str__(self):
        return self.review_title
