from django.db import models
from apps.common.models import BaseModel
from apps.movies.models import Country, Language, Movie, MovieSubtitle, MovieFile


class WatchSession(BaseModel):
    QUALITY_CHOICES = [
        ("480p", "480p"),
        ("720p", "720p"),
        ("1080p", "1080p"),
    ]
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE)
    device = models.CharField(max_length=200, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    country = models.ForeignKey(Country,on_delete=models.PROTECT, blank=True, null=True)
    subtitle = models.ForeignKey(MovieSubtitle, on_delete=models.PROTECT, blank=True, null=True)
    quality = models.CharField(max_length=10, choices=QUALITY_CHOICES, default='720p')

    def __str__(self):
        return f"WatchSession: {self.movie.title} ({self.language})"

class Like(BaseModel):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    watch_session=models.ForeignKey(WatchSession,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.movie.title
    
class Comment(BaseModel):
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    watch_session=models.ForeignKey(WatchSession,on_delete=models.PROTECT)
    text=models.TextField()

    def __str__(self):
        return self.movie.title 
    