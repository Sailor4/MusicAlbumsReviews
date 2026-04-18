from django.urls import path
from .views import AlbumCreateView, AlbumDetailView, ReviewCreateView, AlbumEditView, AlbumDeleteView, ArtistCreateView

urlpatterns = [
    path('add/', AlbumCreateView.as_view(), name='album-add'),
    path('<int:pk>/', AlbumDetailView.as_view(), name='album-details'),
    path('<int:pk>/review/', ReviewCreateView.as_view(), name='review-add'),
    path('<int:pk>/edit/', AlbumEditView.as_view(), name='album-edit'),
    path('<int:pk>/delete/', AlbumDeleteView.as_view(), name='album-delete'),
    path('artist/add/', ArtistCreateView.as_view(), name='artist-add'),
]
