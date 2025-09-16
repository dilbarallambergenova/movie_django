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


