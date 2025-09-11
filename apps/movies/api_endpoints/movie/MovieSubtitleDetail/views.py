from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.movie.MovieSubtitleDetail.serializers import MovieSubtitleDetailSerializer
from apps.movies.models import MovieSubtitle


class MovieSubtitleDetailView(APIView):
    def get(self,request,pk):
        moviesubtitle=get_object_or_404(MovieSubtitle,id=pk)
        serializer=MovieSubtitleDetailSerializer(moviesubtitle)
        return Response(serializer.data)

__all__=['MovieSubtitleDetailView']