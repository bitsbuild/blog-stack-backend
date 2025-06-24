from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import BlogSerializer,ReviewSerializer,CategorySerializer
from app.models import Reviews,Category,Blog
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from app.permissions import BlogAccessByOwnership,ReviewAccessByOwnership
from django_filters.rest_framework import DjangoFilterBackend
class BlogVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated,BlogAccessByOwnership]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog_writer','blog_categories']
class ReviewVS(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,ReviewAccessByOwnership]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['for_blog','review_writer']
class CategoryVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]