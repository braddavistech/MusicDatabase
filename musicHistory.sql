INSERT into history_artist values (null, "The Kinks", 1964)

INSERT into history_song
select null, "Simple Man", 550, 1973, "Rock", id, "https://i1.sndcdn.com/artworks-000098690696-f3w6ar-t500x500.jpg", "https://www.youtube.com/embed/sMmTkKz60W8"
from  history_artist h
where h.ArtistName = "Lynyrd Skynyrd"