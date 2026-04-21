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
        {'name': 'Metallica', 'is_approved': True},
        {'name': 'Nirvana', 'is_approved': True},
        {'name': 'Led Zeppelin', 'is_approved': True},
        {'name': 'Michael Jackson', 'is_approved': True},
        {'name': 'David Bowie', 'is_approved': True},
        {'name': 'Arctic Monkeys', 'is_approved': True},
        {'name': 'The Weeknd', 'is_approved': True},
        {'name': 'Fleetwood Mac', 'is_approved': True},
        {'name': 'Kendrick Lamar', 'is_approved': True},
        {'name': 'Amy Winehouse', 'is_approved': True},
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
        {'title': 'The Wall', 'artist': 'Pink Floyd', 'year': 1979, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/b/b4/PinkFloydWallCover.jpg'},
        {'title': 'Thriller', 'artist': 'Michael Jackson', 'year': 1982, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/5/55/Michael_Jackson_-_Thriller.png'},
        {'title': 'Nevermind', 'artist': 'Nirvana', 'year': 1991, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/b/b7/NirvanaNevermindalbumcover.jpg'},
        {'title': 'Led Zeppelin IV', 'artist': 'Led Zeppelin', 'year': 1971, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/2/26/Led_Zeppelin_-_Led_Zeppelin_IV.jpg'},
        {'title': 'Rumours', 'artist': 'Fleetwood Mac', 'year': 1977, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/f/fb/Fleetwood_Mac_-_Rumours.png'},
        {'title': 'Back to Black', 'artist': 'Amy Winehouse', 'year': 2006, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/6/67/Amy_Winehouse_-_Back_to_Black.png'},
        {'title': 'Master of Puppets', 'artist': 'Metallica', 'year': 1986, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/b/b2/Metallica_-_Master_of_Puppets_cover.jpg'},
        {'title': 'AM', 'artist': 'Arctic Monkeys', 'year': 2013, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/0/04/Arctic_Monkeys_-_AM.png'},
        {'title': 'After Hours', 'artist': 'The Weeknd', 'year': 2020, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/c/c1/The_Weeknd_-_After_Hours.png'},
        {'title': 'To Pimp a Butterfly', 'artist': 'Kendrick Lamar', 'year': 2015, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/f/f6/Kendrick_Lamar_-_To_Pimp_a_Butterfly.png'},
        {'title': 'The Rise and Fall of Ziggy Stardust', 'artist': 'David Bowie', 'year': 1972, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/0/01/ZiggyStardust.jpg'},
        {'title': 'In Rainbows', 'artist': 'Radiohead', 'year': 2007, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/2/2e/In_Rainbows_official_cover.png'},
        {'title': 'Let It Be', 'artist': 'The Beatles', 'year': 1970, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/2/25/LetItBe.jpg'},
        {'title': 'Plastic Beach', 'artist': 'Gorillaz', 'year': 2010, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/d/d1/Plasticbeach452.jpg'},
        {'title': 'News of the World', 'artist': 'Queen', 'year': 1977, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/e/ea/Queen_News_Of_The_World.png'},
        {'title': 'Ride the Lightning', 'artist': 'Metallica', 'year': 1984, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/f/f4/Ridethelighning.jpg'},
        {'title': 'In Utero', 'artist': 'Nirvana', 'year': 1993, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/e/e5/In_Utero_%28Nirvana%29_album_cover.jpg'},
        {'title': 'Physical Graffiti', 'artist': 'Led Zeppelin', 'year': 1975, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/e/e3/Led_Zeppelin_-_Physical_Graffiti.jpg'},
        {'title': 'Starboy', 'artist': 'The Weeknd', 'year': 2016, 'format': 'CD',
         'url': 'https://upload.wikimedia.org/wikipedia/en/3/39/The_Weeknd_-_Starboy.png'},
        {'title': 'Hunky Dory', 'artist': 'David Bowie', 'year': 1971, 'format': 'VNL',
         'url': 'https://upload.wikimedia.org/wikipedia/en/4/41/DavidBowieHunkyDory.jpg'},
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