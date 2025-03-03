from django.test import TestCase, Client
from music.models import Artist, Album, Song


class TestArtistViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        self.artist = Artist.objects.create(name='Test Artist')

    def test_get_info(self):
        response = self.client.get('/artists/')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], 'Test Artist')
        self.assertIsNotNone(data[0]['id'])


class TestSongViewSet(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(artist=self.artist, title='Test Album')
        self.song = Song.objects.create(album=self.album, title='Test Song')
        self.client = Client()

    def test_search(self):
        response = self.client.get('/songs/?search=Test Song')
        data = response.data

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Test Song')