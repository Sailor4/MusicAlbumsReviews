from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Album, Review
from .forms import AlbumCreateForm, ReviewCreateForm
from django.shortcuts import get_object_or_404
from django.db.models import Avg


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()
        average = reviews.aggregate(Avg('rating'))['rating__avg']
        count = reviews.count()

        context['average_rating'] = round(average, 1) if average else "No ratings"
        context['reviews_count'] = count
        return context


class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewCreateForm
    template_name = 'albums/review-add.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = get_object_or_404(Album, pk=self.kwargs.get('pk'))
        return context

    def form_valid(self, form):
        album_id = self.kwargs.get('pk')
        album = get_object_or_404(Album, pk=album_id)
        form.instance.album = album
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.kwargs.get('pk')})


class AlbumEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Album
    form_class = AlbumCreateForm
    template_name = 'albums/album-edit.html'

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.pk})

    def test_func(self):
        album = self.get_object()
        is_owner = self.request.user == album.added_by
        is_not_approved = not album.is_approved

        return is_owner and is_not_approved

    def get_success_url(self):
        return reverse_lazy('album-details', kwargs={'pk': self.object.pk})


class AlbumDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Album
    template_name = 'albums/album-delete.html'
    success_url = reverse_lazy('my-albums')

    def test_func(self):
        album = self.get_object()
        return self.request.user == album.added_by
