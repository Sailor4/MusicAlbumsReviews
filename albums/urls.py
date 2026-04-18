from django.urls import path
from .views import AlbumCreateView, AlbumDetailView, ReviewCreateView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='album-add'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-details'),
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='review-add'),
]
