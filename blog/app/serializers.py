from rest_framework import serializers
from app.models import (
                        Blog,
                        Review,
                        Category,
                        )
class BlogSerializer(serializers.ModelSerializer):
    blog_writer = serializers.PrimaryKeyRelatedField(read_only=True)
    blog_id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    review_id = serializers.UUIDField(read_only=True)
    review_writer = serializers.StringRelatedField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
class CategorySerializer(serializers.ModelSerializer):
    category_id = serializers.UUIDField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)
    class Meta:
        model = Category
        fields = '__all__'