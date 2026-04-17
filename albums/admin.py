from django.contrib import admin
from .models import Artist, Album, Song


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