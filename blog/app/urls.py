from django.urls import path,include
from rest_framework.routers import DefaultRouter
from app.views import BlogVS,ReviewVS,CategoryVS
router = DefaultRouter()
router.register(r'blogs',BlogVS,basename='blogs')
router.register(r'review',ReviewVS,basename='review')
router.register(r'category',CategoryVS,basename='category')
urlpatterns = router.urls