from django.db import models
import uuid
from django.contrib.auth.models import User
class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    category_name = models.CharField(max_length=150)
    def __str__(self):
        return self.category_name
class Reviews(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    review_writer = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    review_title = models.CharField(max_length=150)
    review_body = models.CharField(max_length=1500)
    review_created = models.DateTimeField(auto_now_add=True,editable=False)
    review_updated = models.DateTimeField(auto_now=True,editable=False)
    def __str__(self):
        return self.review_title
class Blog(models.Model):
    blog_id = models.UUIDField(default=uuid.uuid4,editable=False,primary_key=True)
    blog_writer = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    blog_title = models.CharField(max_length=150)
    blog_body = models.CharField(max_length=7500)
    blog_categories = models.ManyToManyField(Category,related_name='blogs')
    blog_reviews = models.ManyToManyField(Reviews,related_name='blogs')
    blog_created = models.DateTimeField(auto_now_add=True,editable=False)
    blog_updated = models.DateTimeField(auto_now=True,editable=False)
    def __str__(self):
        return self.blog_title