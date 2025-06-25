from rest_framework.serializers import ModelSerializer,SlugRelatedField,StringRelatedField
from app.models import Category,Blog,Reviews
class ReviewSerializer(ModelSerializer):
    review_writer = StringRelatedField()
    for_blog = StringRelatedField()
    class Meta:
        model = Reviews
        fields = '__all__'
class BlogSerializer(ModelSerializer):
    blog_categories = SlugRelatedField(many=True,queryset=Category.objects.all(),slug_field='category_name')
    reviews = ReviewSerializer(many=True,read_only=True)
    blog_writer = StringRelatedField(read_only=True)
    class Meta:
        model = Blog
        fields = '__all__'
    def create(self, validated_data):
        validated_data['blog_writer'] = self.context['request'].user
        return super().create(validated_data)
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'