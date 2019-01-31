# Create your models here.
from django.db import models
from django.utils import timezone


# Create your models here.
class Artist(models.Model):
  ArtistName = models.CharField(max_length = 50)
  YearEstablished = models.IntegerField(default = 2019)
  def __str__(self):
    return self.ArtistName
  def was_published_recently(self):
        return self.YearEstablished
  def name(self):
    return self.ArtistName


class Song(models.Model):
    Title = models.CharField(max_length = 50)
    SongLength = models.IntegerField(default = 0)
    ReleaseDate = models.IntegerField(default = 2019)
    Genre = models.CharField(max_length = 50)
    Art = models.CharField(max_length = 200)
    Video = models.CharField(max_length = 200)
    ArtistId = models.ForeignKey(Artist, on_delete=models.CASCADE)
    def __str__(self):
      return self.Title
    def title(self):
      return self.Title
    def length(self):
      return self.SongLength
    def releaseDate(self):
      return self.ReleaseDate
    def genre(self):
      return self.Genre
    def artistId(self):
      return self.ArtistId