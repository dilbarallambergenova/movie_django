from django.urls import path
# from .views import (
#                language_list_api_view,
#                genre_list_api_view,
#                country_list_api_view,
#                movie_list_api_view,
#                   )
from apps.movies.api_endpoints.movie import MovieDetail,MovieAudioDetail
from apps.movies.api_endpoints import genre

urlpatterns=[
    # path('language_api',language_list_api_view,name='language_list'),
    # path('genre_api',genre_list_api_view,name='genre_list'),
    # path('country_api',country_list_api_view,name='country_list'),
    # path('movie_api',movie_list_api_view,name='movie_list'),
    path('<int:pk>/',MovieDetail.MovieDetailView.as_view(),name='movie_detail'),
    path('<int:pk>/audios',MovieAudioDetail.MovieAudioDetailView.as_view(),name='movieaudio_detail'),
    path('genres/', genre.GenreListView.as_view(), name='genres_list'),


]