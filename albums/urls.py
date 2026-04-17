from django.urls import path
from .views import AlbumCreateView, AlbumDetailView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='album-add'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-details'),
]
