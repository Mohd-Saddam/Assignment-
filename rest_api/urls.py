from django.urls import path,include
from .views import (CategoryListAPIView, MainListAPIView)


urlpatterns = [
    path('api/main', MainListAPIView.as_view(), name='main_api'),
    path('api/category_list', CategoryListAPIView.as_view(), name='category_list_api'),
]