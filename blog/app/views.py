from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from app.models import (
                        Blog,
                        Review,
                        Category,
                        )
from app.serializers import (
                            BlogSerializer,
                            ReviewSerializer,
                            CategorySerializer,
                            )
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['blog_writer','blog_categories']
    def perform_create(self, serializer):
        serializer.save(blog_writer=self.request.user)
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review_writer']
    def perform_create(self, serializer):
        serializer.save(review_writer=self.request.user)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer