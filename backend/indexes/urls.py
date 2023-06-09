"""
路由配置
"""
from django.urls import path, include
from .views import build_index, test_search, TermViewSet, PostingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('term', TermViewSet)
router.register('posting', PostingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('build_index/', build_index),
    path('test_search/', test_search),
]