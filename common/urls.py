from django.urls import path
from common.views import HomePageView, MyAlbumsView, AlbumSearchView, ContactView, SignUpView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-albums/', MyAlbumsView.as_view(), name='my-albums'),
    path('search/', AlbumSearchView.as_view(), name='album-search'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('signup/', SignUpView.as_view(), name='signup'),
]
