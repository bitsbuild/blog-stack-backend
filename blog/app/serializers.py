from rest_framework.serializers import ModelSerializer
from app.models import Category,Blog,Reviews
class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Reviews
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'