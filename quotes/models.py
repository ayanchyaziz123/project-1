from django.db import models

# Create your models here.

class Album(models.Model):
    albumName = models.CharField(max_length=200)

    def __str__(self):
          return self.albumName

class Song(models.Model):
    song_name = models.CharField(max_length=200)
    song_lyrics = models.TextField()

    album_cat = models.ForeignKey(
        'Album',
        on_delete= models.CASCADE

    )

    def __str__(self):
        if len(self.song_lyrics)> 50 :
            return self.song_lyrics[:50] + "..."
        else:
            return self.song_lyrics
