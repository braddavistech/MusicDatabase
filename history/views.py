from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Artist, Song

def index(request):
  all_artists = Artist.objects.all()
  context = {"all_artists": all_artists}
  return render(request, "history/artist.html", context)

def detail(request, pk):
  artist = get_object_or_404(Artist, id = pk)
  context = {"artist": artist}
  return render(request, "history/detail.html", context)

def addArtist(request):
  return render(request, "history/addArtist.html")

def save_artist(request):
  name = request.POST['artist_name']
  date = request.POST['artist_date']
  a = Artist(ArtistName = name, YearEstablished = int(date))
  a.save()
  response = redirect('/')
  return response

def save_song(request):
  song_artist = request.POST['song_artist']
  song_title = request.POST['song_title']
  song_length = request.POST['song_length']
  song_release = request.POST['song_release']
  song_genre = request.POST['song_genre']
  song_art = request.POST['song_art']
  song_video = request.POST['song_video']
  s = Song(Title = song_title, SongLength = int(song_length), ReleaseDate = int(song_release), Genre = song_genre, ArtistId_id = int(song_artist), Art = song_art, Video = song_video)
  s.save()
  response = redirect('/')
  return response

def addSong(request):
  all_artists = Artist.objects.all()
  context = {"all_artists": all_artists}
  return render(request, "history/addSong.html", context)

def submit_artist(request, name, date):
  context = {"name": name, "date": date}
  return render(request, 'history/newArtist.html', context)

