from django.db import models
from apps.common.models import BaseModel


class Genre(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Language(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Country(BaseModel):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Movie(BaseModel):
    title = models.CharField(max_length=255)

    country = models.ForeignKey(Country, on_delete=models.PROTECT)
    description = models.TextField(blank=True, null=True)
    age_restriction = models.PositiveSmallIntegerField(default=0)
    release_year = models.DateField(null=True, blank=True)
    genres = models.ManyToManyField("Genre", related_name="movies")

    def __str__(self):
        return self.title


class MovieAudio(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    name = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.movie.title} ({self.language} audio)"


class MovieSubtitle(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.movie.title} ({self.language} subtitle)"


class PosterImage(BaseModel):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    image = models.ImageField(upload_to="movies/posters/")

    def __str__(self):
        return f"Poster for {self.movie.title} ({self.language})"


class MovieFile(BaseModel):
    quality_choices = [
        ("480p", "480p"),
        ("720p", "720p"),
        ("1080p", "1080p"),
    ]

    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    file = models.FileField(upload_to="movies/videos")
    quality = models.CharField(max_length=20, choices=quality_choices, default="720p")

    def __str__(self):
        return f"File: {self.movie.title} ({self.language})"

class WatchSession(BaseModel):
    quality_choices = [
        ("480p", "480p"),
        ("720p", "720p"),
        ("1080p", "1080p"),
    ]
    device_choices = [
        ("MOBILE", 'Mobile'),
        ("TABLET", 'Tablet'),
        ("PC", 'PC'),
        ("SMARTTV", 'SmartTV'),
    ]
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    device=models.CharField(max_length=20,choices=device_choices,default="Mobile")
    language=models.ForeignKey(Language,on_delete=models.PROTECT)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)
    subtitle=models.ForeignKey(MovieSubtitle,on_delete=models.CASCADE)
    quality=models.CharField(max_length=20,choices=quality_choices,default="720p")
    def __str__(self):
        return f"WatchSession: {self.movie.title} ({self.language})"