from django import forms
from .models import Album, Review, Artist


class AlbumCreateForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'artist', 'release_year', 'music_format', 'image_url']

        labels = {
            'title': 'Album Title',
            'artist': 'Artist / Band',
            'release_year': 'Year of Release',
            'music_format': 'Format',
            'image_url': 'Cover Image URL (optional)',
        }

        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter album title...'}),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://example.com/image.jpg'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        artist_field = self.fields.get('artist')
        if artist_field:
            artist_field.queryset = Artist.objects.filter(is_approved=True)


class ReviewCreateForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={
                'placeholder': 'Write a review about this album...',
                'rows': 4
            }),
        }


class ArtistCreateForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields = ['name']
