from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model

UserModel = get_user_model()

NAME_MAX_LENGTH = 100
TITLE_MAX_LENGTH = 150
FORMAT_MAX_LENGTH = 10
MIN_RELEASE_YEAR = 1900
MAX_RELEASE_YEAR = 2026
SONG_NAME_MAX_LENGTH = 100
COMMENT_MAX_LENGTH = 500


class Artist(models.Model):
    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        unique=True
    )

    def __str__(self):
        return self.name


class Album(models.Model):
    VINYL = 'Vinyl'
    CD = 'CD'
    SACD = 'SACD'

    FORMAT_CHOICES = [
        (VINYL, 'Vinyl'),
        (CD, 'CD'),
        (SACD, 'SACD'),
    ]

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH
    )

    artist = models.ForeignKey(
        Artist,
        on_delete=models.CASCADE,
        related_name='albums'
    )

    release_year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(MIN_RELEASE_YEAR),
            MaxValueValidator(MAX_RELEASE_YEAR)
        ]
    )

    music_format = models.CharField(
        max_length=FORMAT_MAX_LENGTH,
        choices=FORMAT_CHOICES
    )

    image_url = models.URLField(
        blank=True,
        null=True
    )

    is_approved = models.BooleanField(
        default=False
    )

    added_by = models.ForeignKey(
        UserModel,
        on_delete=models.SET_NULL,
        null=True
    )

    def __str__(self):
        return f"{self.title} by {self.artist.name} ({self.music_format})"


class Song(models.Model):
    title = models.CharField(
        max_length=SONG_NAME_MAX_LENGTH
    )
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='songs'
    )
    duration = models.DurationField(
        help_text="Format: MM:SS",
        null=True,
        blank=True
    )

    def __str__(self):
        return f"{self.title} ({self.album.title})"


class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    comment = models.TextField(
        max_length=COMMENT_MAX_LENGTH,
        blank=True,
        null=True
    )

    rating = models.IntegerField(
        choices=RATING_CHOICES
    )

    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    user = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name='reviews'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Review for {self.album.title} by {self.user.username}"