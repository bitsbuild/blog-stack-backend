from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import BlogSerializer,ReviewSerializer,CategorySerializer
from app.models import Reviews,Category,Blog
class BlogVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
class ReviewVS(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
class CategoryVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer