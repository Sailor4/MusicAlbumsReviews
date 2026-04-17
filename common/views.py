from django.views.generic import ListView
from albums.models import Album

class HomePageView(ListView):
    model = Album
    template_name = 'common/home.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.filter(is_approved=True).order_by('-release_year')