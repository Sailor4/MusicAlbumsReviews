from django.urls import path
from common.views import HomePageView, MyAlbumsView, AlbumSearchView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-albums/', MyAlbumsView.as_view(), name='my-albums'),
    path('search/', AlbumSearchView.as_view(), name='album-search'),
]
