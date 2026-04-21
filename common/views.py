from django.views.generic import ListView, TemplateView, FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.core.mail import send_mail
from django.db.models import Q, Avg
from albums.models import Album, Artist
from .forms import ContactForm, AppUserCreationForm
from django.shortcuts import render


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


class ContactView(SuccessMessageMixin, FormView):
    template_name = 'common/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('home')
    success_message = "Your message was sent successfully! We will get back to you soon."

    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        name = form.cleaned_data['name']
        user_email = form.cleaned_data['email']
        content = form.cleaned_data['message']
        full_message = f"Message from {name} ({user_email}):\n\n{content}"

        send_mail(
            subject=subject,
            message=full_message,
            from_email=user_email,
            recipient_list=['admin@music-albums-reviews.com'],
            fail_silently=False,
        )
        return super().form_valid(form)


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = AppUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    success_message = "Your account was created successfully!"


def handler404(request, exception):
    return render(request, '404.html', status=404)


def handler500(request):
    return render(request, '500.html', status=500)
