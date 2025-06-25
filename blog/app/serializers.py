from rest_framework.serializers import ModelSerializer,SlugField,StringRelatedField
from app.models import Category,Blog,Reviews
class ReviewSerializer(ModelSerializer):
    review_writer = StringRelatedField()
    for_blog = StringRelatedField()
    class Meta:
        model = Reviews
        fields = '__all__'
class BlogSerializer(ModelSerializer):
    blog_categories = StringRelatedField(read_only=True,many=True)
    reviews = ReviewSerializer(many=True,read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'