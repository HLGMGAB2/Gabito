from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    MemorialListView,
    MemorialDetailView,
    MemorialCreateView,
    MemorialUpdateView,
    MemorialDeleteView
)

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('memorials/', MemorialListView.as_view(), name='memorial_list'),
    path('memorials/<int:pk>/', MemorialDetailView.as_view(), name='memorial_detail'),
    path('memorials/create/', MemorialCreateView.as_view(), name='memorial_form'),
    path('memorials/<int:pk>/update/', MemorialUpdateView.as_view(), name='memorial_update'),
    path('memorials/<int:pk>/delete/', MemorialDeleteView.as_view(), name='memorial_delete'),
]