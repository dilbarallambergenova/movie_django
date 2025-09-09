from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from  .models import (
                     Language,
                     Genre,
                     Country,
                     Movie,
                     )
from .serializers import (
                    LanguageListSerializer,
                    GenreListSerializer,
                    CountryListSerializer,
                    MovieListSerializer,
                    ) 

@api_view(['GET'])
def language_list_api_view(request):
    languages=Language.objects.all()
    serializer=LanguageListSerializer(languages,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def genre_list_api_view(request):
    genres=Genre.objects.all()
    serializer=GenreListSerializer(genres,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def country_list_api_view(request):
    countrys=Country.objects.all()
    serializers=CountryListSerializer(countrys,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_list_api_view(request):
    movies=Country.objects.all()
    serializer=MovieListSerializer(movies,many=True)
    return Response(serializer.data)