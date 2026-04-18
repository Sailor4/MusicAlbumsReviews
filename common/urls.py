from django.urls import path
from common.views import HomePageView, MyAlbumsView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my-albums/', MyAlbumsView.as_view(), name='my-albums'),
]
