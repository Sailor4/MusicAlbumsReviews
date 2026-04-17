from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Album
from .forms import AlbumCreateForm


class AlbumCreateView(LoginRequiredMixin, CreateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-create.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.added_by = self.request.user

        return super().form_valid(form)

from django.views.generic import DetailView
from .models import Album

class AlbumDetailView(DetailView):
    model = Album
    template_name = 'albums/album-details.html'
    context_object_name = 'album'