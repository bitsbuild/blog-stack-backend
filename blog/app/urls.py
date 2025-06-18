from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import (
                        BlogViewSet,
                        ReviewViewSet,
                        CategoryViewSet,
                      )
router = DefaultRouter()
router.register(r'blogs',BlogViewSet,basename='blogs')
router.register(r'reviews',ReviewViewSet,basename='reviews')
router.register(r'categories',CategoryViewSet,basename='categories')
urlpatterns = router.urls