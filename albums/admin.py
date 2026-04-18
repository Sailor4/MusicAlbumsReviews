from django.contrib import admin
from .models import Artist, Album, Song, Review


class SongInline(admin.TabularInline):
    model = Song
    extra = 3

@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist', 'music_format', 'release_year', 'is_approved')
    list_display_links = ('title',)
    list_filter = ('music_format', 'is_approved', 'release_year')
    search_fields = ('title', 'artist__name')
    list_editable = ('is_approved',)
    inlines = [SongInline]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('album', 'user', 'rating', 'created_at')
    list_filter = ('rating', 'created_at')
    search_fields = ('album__title', 'user__username')