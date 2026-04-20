from django.views.generic import ListView, TemplateView
from albums.models import Album, Artist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Avg


class HomePageView(TemplateView):
    template_name = 'common/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_albums'] = Album.objects.filter(is_approved=True).order_by('-id')[:6]
        context['popular_albums'] = Album.objects.filter(is_approved=True) \
            .annotate(avg_rating=Avg('reviews__rating')) \
            .order_by('-avg_rating')[:6]

        return context


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


class AlbumSearchView(ListView):
    model = Album
    template_name = 'common/search.html'
    context_object_name = 'albums'

    def get_queryset(self):
        queryset = Album.objects.filter(is_approved=True)
        query = self.request.GET.get('search')
        genre = self.request.GET.get('genre')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(artist__name__icontains=query)
            )
        if genre:
            queryset = queryset.filter(music_format=genre)

        return queryset.order_by('-release_year')
