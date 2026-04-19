from django.views.generic import ListView
from albums.models import Album, Artist
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['my_artists'] = Artist.objects.filter(added_by=self.request.user).order_by('name')
        return context