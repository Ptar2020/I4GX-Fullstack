from django.db import models
import datetime
import django


class Artiste(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    age = models.IntegerField()
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Song(models.Model):
    title = models.CharField(max_length = 250)
    date_released = models.DateField(default = django.utils.timezone.now)#datetime.datetime.now())
    likes = models.IntegerField(default = 0)
    artiste_id = models.ForeignKey(Artiste, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.title} - {self.artiste_id}"
    
class Lyric(models.Model):
    content = models.TextField(null=True)
    song_id = models.ForeignKey(Song, on_delete = models.CASCADE)
    
    def __str__(self):
        return f"{self.song_id}"
