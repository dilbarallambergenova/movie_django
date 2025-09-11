from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.movies.api_endpoints.movie.MovieFileDetail.serializers import MovieFileDetailSerializer
from apps.movies.models import MovieFile


class MovieFileDetailView(APIView):
    def get(self,request,pk):
        moviefile=get_object_or_404(MovieFile,id=pk)
        serializer=MovieFileDetailSerializer(moviefile)
        return Response(serializer.data)

__all__=['MovieFileDetailView']