from django.views.generic import ListView
from albums.models import Album
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(ListView):
    model = Album
    template_name = 'common/home.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(is_approved=True).order_by('-release_year')


class MyAlbumsView(LoginRequiredMixin, ListView):
    model = Album
    template_name = 'common/my-albums.html'
    context_object_name = 'my_albums'

    def get_queryset(self):
        return Album.objects.filter(added_by=self.request.user).order_by('-release_year')