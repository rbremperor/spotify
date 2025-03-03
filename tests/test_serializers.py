from django.test import TestCase
from music.models import Artist, Album
from music.serializers import ArtistSerializer, SongSerializer

class TestArtistSerializer(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Test Artist')

    def test_date(self):
        data = ArtistSerializer(self.artist).data
        assert data['id'] is not None
        assert data['name'] == 'Test Artist'
        assert data['picture'] == ''

class TestSongSerializer(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='Test Artist')
        self.album = Album.objects.create(artist=self.artist,title='Test Album')

    def test_is_valid(self):
        data = {
            "title": "Test Song",
            "album": self.album.id,  # Ensure it's an ID, not a dictionary
            "cover": "",  # Ensure it's not None
            "source": "http://example.com/music.mp3",  # Ensure it's a valid URL
            "listened": 0
        }
        serializer = SongSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_is_not_invalid(self):
        data = {
            "title": "Test Song",
            "cover": "",
            "source": "http://example.com/music",
            "album": self.album.id,
            "listened": 0
        }
        serializer = SongSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        print(serializer.errors)
        self.assertEqual(str(serializer.errors['source'][0]), "Mp3 file is required")
