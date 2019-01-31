from django.test import TestCase
from django.urls import reverse
from .models import Artist, Song

# Create your tests here.

#Stuff to test
#TODO: context: what we send to the template
#TODO: content: the render html
#TODO: response

# Name all tests with test_(testname)

#Test client is a Python class that acts as a dummy web browser

#simulate GET and POST requests
#see chain of redirect
#check context and content

#separate TestClass for each model or view
#separate test method for each condition

class ArtistTest(TestCase):

  def test_list_artists(self):
    new_artist = Artist.objects.create(
      ArtistName="Test Group",
      YearEstablished="2019"
    )

    response = self.client.get(reverse('history:index'))

    self.assertEqual(response.status_code, 200)

    self.assertEqual(len(response.context['all_artists']), 1)

    self.assertIn(new_artist.ArtistName.encode(), response.content)


  # def test_get_artist(self):

  #   # url to grab data for adding artist form
  #   response = self.client.get(reverse('addArtist'))

  #   # grabs one input from form and checks existance
  #   self.assertIn(
  #     '<input class="input_field" id="artist_date" type="text" name="artist_date" placeholder="Enter year artist/group was established here.">'.encode(), response.content)

  def test_post_artist(self):

    response = self.client.post(reverse('history:save_artist'), {'artist_name': "Bob Fellers", "artist_date": 1977})

    self.assertEqual(response.status_code, 302)


class SongTest(TestCase):

  def test_post_song(self):

    response = self.client.post(reverse('history:save_song'), {"song_title": "Song Title",
      "song_length": 265,
      "song_release": 1975,
      "song_genre": "Rock",
      "song_art": "Art url",
      "song_video": "Video url",
      "song_artist": 1})

    self.assertEqual(response.status_code, 302)
