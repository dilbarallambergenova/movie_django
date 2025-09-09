from django.db import models
from apps.common.models import BaseModel

class Language(BaseModel):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Country(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
   

class Genre(BaseModel):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Movie(BaseModel):
    movie_genre=models.ManyToManyField('Genre',related_name='movies')
    title=models.CharField(max_length=100)
    country=models.ForeignKey(Country, on_delete=models.PROTECT)
    description=models.PositiveSmallIntegerField(default=0)
    age_restriction=models.DateField()
    year=models.IntegerField()

    def __str__(self):
        return self.title


class MovieAudio(BaseModel):
    language=models.ForeignKey(Language,on_delete=models.PROTECT)
    name=models.CharField(max_length=100)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class MovieSubtitle(BaseModel):
    language=models.ForeignKey(Language,on_delete=models.PROTECT)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)

    def __str__(self):
        return self.movie.name
     

class MovieFile(BaseModel):
    language=models.ForeignKey(Language,on_delete=models.PROTECT)
    movie=models.ForeignKey(Movie,on_delete=models.PROTECT)
    file=models.FileField(upload_to='movies/files')

    def __str__(self):
        return self.movie.name

class PosterImage(BaseModel):
    movie=models.ForeignKey(Movie,on_delete=models.PROTECT)
    language=models.ForeignKey(Language,on_delete=models.PROTECT)
    image=models.ImageField(upload_to='movies/image')

    def __str__(self):
        return self.movie.name
    
