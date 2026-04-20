import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MusicAlbumsReviews.settings')
django.setup()

from django.contrib.auth import get_user_model
from albums.models import Artist, Album, Review

User = get_user_model()


def seed():
#users
    user, _ = User.objects.get_or_create(username='testuser', email='test@test.com')
    if not user.password:
        user.set_password('pass1234')
        user.save()
    print(f"We are using user: {user.username}")

#artists
    artists_data = [
        {'name': 'Pink Floyd', 'is_approved': True},
        {'name': 'Queen', 'is_approved': True},
        {'name': 'Daft Punk', 'is_approved': True},
        {'name': 'Radiohead', 'is_approved': True},
        {'name': 'Gorillaz', 'is_approved': True},
        {'name': 'The Beatles', 'is_approved': True},
    ]

    artists = {}
    for data in artists_data:
        artist, _ = Artist.objects.get_or_create(name=data['name'],
                                                 defaults={'added_by': user, 'is_approved': data['is_approved']})
        artists[data['name']] = artist
    print(f"Artists Added: {len(artists)}")

#albums
    albums_data = [
        {'title': 'The Dark Side of the Moon', 'artist': 'Pink Floyd', 'year': 1973, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/3/3b/Dark_Side_of_the_Moon.png'},
        {'title': 'A Night at the Opera', 'artist': 'Queen', 'year': 1975, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/4/4d/Queen_A_Night_At_The_Opera.png'},
        {'title': 'Discovery', 'artist': 'Daft Punk', 'year': 2001, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/2/27/Daft_Punk_-_Discovery.jpg'},
        {'title': 'OK Computer', 'artist': 'Radiohead', 'year': 1997, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/b/ba/Radioheadokcomputer.png'},
        {'title': 'Demon Days', 'artist': 'Gorillaz', 'year': 2005, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/d/df/Gorillaz_Demon_Days.png'},
        {'title': 'Abbey Road', 'artist': 'The Beatles', 'year': 1969, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/4/42/Beatles_-_Abbey_Road.jpg'},
        {'title': 'Random Access Memories', 'artist': 'Daft Punk', 'year': 2013, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/a/a7/Random_Access_Memories.jpg'},
    ]

    for data in albums_data:
        Album.objects.get_or_create(
            title=data['title'],
            defaults={
                'artist': artists[data['artist']],
                'release_year': data['year'],
                'music_format': data['format'],
                'image_url': data['url'],
                'added_by': user,
                'is_approved': True
            }
        )
    print("Albums Added")

#reviews
    all_albums = Album.objects.all()
    reviews_texts = ["Masterpiece!", "Sounds great on vinyl.", "Overrated but good.", "A must have!", "Pure art."]

    import random
    for album in all_albums:
        if not album.reviews.exists():
            Review.objects.create(
                album=album,
                user=user,
                rating=random.randint(3, 5),
                comment=random.choice(reviews_texts)
            )
    print("Reviews Added")
    print("All Done.")


if __name__ == '__main__':
    seed()