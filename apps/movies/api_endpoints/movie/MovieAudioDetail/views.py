from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.movie.MovieAudioDetail.serializers import MovieAudioDetailSerializer
from apps.movies.models import MovieAudio



class MovieAudioDetailView(APIView):
    def get(self,request,pk):
        movieaudio=get_object_or_404(MovieAudio,id=pk)
        serializer=MovieAudioDetailSerializer(movieaudio)
        return Response(serializer.data)

__all__=['MovieAudioDetailView']