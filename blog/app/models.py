from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
import uuid
class Category(models.Model):
    category_id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    category_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['category_name'],
                name = 'unique_category'
            )
        ]
    def __str__(self):
        return self.category_name
class Blog(models.Model):
    blog_id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    blog_writer = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    blog_title = models.CharField(max_length=80)
    blog_body = models.CharField(max_length=1000)
    blog_categories = models.ManyToManyField(Category,related_name='category_blog',blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    class Meta:    
        constraints = [
            models.UniqueConstraint(
                fields=['blog_title'],
                name='unique_blog_title'
            )
        ]
    def __str__(self):
        return self.blog_title
class Review(models.Model):
    review_id = models.UUIDField(default=uuid.uuid4,primary_key=True,editable=False)
    review_writer = models.ForeignKey(User,on_delete=models.CASCADE,editable=False)
    review_body = models.CharField(max_length=250)
    review_blog = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='review')
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True,editable=False)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['review_blog','review_writer'],
                name='one_review_per_blog_per_user',
            )
        ]
    def __str__(self):
        return str(self.review_writer.username)