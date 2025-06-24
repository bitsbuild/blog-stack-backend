from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from app.serializers import BlogSerializer,ReviewSerializer,CategorySerializer
from app.models import Reviews,Category,Blog
from rest_framework.throttling import UserRateThrottle
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from app.permissions import BlogAccessByOwnership,ReviewAccessByOwnership
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
class BlogVS(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated,BlogAccessByOwnership]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['blog_writer','blog_categories']
    search_fields = ['blog_writer','blog_title','blog_body']
class ReviewVS(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated,ReviewAccessByOwnership]
    throttle_classes = [UserRateThrottle]
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['for_blog','review_writer']
    search_fields = ['review_writer','review_title','review_body']
class CategoryVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]