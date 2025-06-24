from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import BlogSerializer,ReviewSerializer,CategorySerializer
from app.models import Reviews,Category,Blog
from rest_framework.throttling import UserRateThrottle
class BlogVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    throttle_classes = [UserRateThrottle]
class ReviewVS(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    throttle_classes = [UserRateThrottle]
class CategoryVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer