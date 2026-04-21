from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Artist, Album, Review

User = get_user_model()

class MusicAppTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='owner', password='pass123')
        self.other_user = User.objects.create_user(username='other', password='pass123')
        self.client = Client()

        self.artist = Artist.objects.create(name="Legendary Band", added_by=self.user)

        self.album = Album.objects.create(
            title="First Album",
            artist=self.artist,
            release_year=2020,
            music_format='CD',
            added_by=self.user,
            is_approved=False
        )

    def test_artist_str(self):
        self.assertEqual(str(self.artist), "Legendary Band")

    def test_album_str(self):
        self.assertEqual(str(self.album), "First Album by Legendary Band (CD)")

    def test_album_initial_approval_is_false(self):
        self.assertFalse(self.album.is_approved)

    def test_review_creation(self):
        review = Review.objects.create(album=self.album, user=self.user, rating=5, comment="Great!")
        self.assertEqual(review.rating, 5)

    def test_artist_added_by_link(self):
        self.assertEqual(self.artist.added_by.username, 'owner')

    def test_album_format_choices(self):
        self.assertEqual(self.album.music_format, 'CD')

    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_album_details_status_code(self):
        response = self.client.get(reverse('album-details', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 200)

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_page_status_code(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_search_status_code(self):
        response = self.client.get(reverse('album-search'))
        self.assertEqual(response.status_code, 200)

    def test_protected_page_redirects_anonymous(self):
        response = self.client.get(reverse('album-add'))
        self.assertEqual(response.status_code, 302)

    def test_owner_can_access_edit_page(self):
        self.client.login(username='owner', password='pass123')
        response = self.client.get(reverse('album-edit', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 200)

    def test_non_owner_cannot_edit_album(self):
        self.client.login(username='other', password='pass123')
        response = self.client.get(reverse('album-edit', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 403)

    def test_cannot_edit_approved_album(self):
        self.album.is_approved = True
        self.album.save()
        self.client.login(username='owner', password='pass123')
        response = self.client.get(reverse('album-edit', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 403)

    def test_user_can_post_review(self):
        self.client.login(username='owner', password='pass123')
        response = self.client.post(reverse('review-add', kwargs={'pk': self.album.pk}), {
            'rating': 4,
            'comment': 'Good one'
        })
        self.assertEqual(Review.objects.count(), 1)

    def test_user_cannot_post_two_reviews_for_same_album(self):
        Review.objects.create(album=self.album, user=self.user, rating=5)
        self.client.login(username='owner', password='pass123')
        response = self.client.get(reverse('review-add', kwargs={'pk': self.album.pk}))
        self.assertEqual(response.status_code, 302)

    def test_logout_functionality(self):
        self.client.login(username='owner', password='pass123')
        response = self.client.post(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_delete_album_owner_only(self):
        self.client.login(username='other', password='pass123')
        response = self.client.post(reverse('album-delete', kwargs={'pk': self.album.pk}))
        self.assertTrue(Album.objects.filter(pk=self.album.pk).exists())

    def test_artist_edit_logic_not_approved(self):
        self.client.login(username='owner', password='pass123')
        response = self.client.get(reverse('artist-edit', kwargs={'pk': self.artist.pk}))
        self.assertEqual(response.status_code, 200)