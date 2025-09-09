from rest_framework import serializers
from .models import (
                    Language,
                    Genre,
                    Country,
                    Movie,
                    ) 

class LanguageListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Language
        fields='__all__'

class GenreListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Genre
        fields='__all__'

class CountryListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields='__all__'

class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Movie
        fields='__all__'
