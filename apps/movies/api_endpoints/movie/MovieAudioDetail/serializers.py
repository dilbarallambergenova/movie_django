from rest_framework import serializers

from apps.movies.models import MovieAudio
from apps.movies.api_endpoints.language import LanguageMiniSerializer

class MovieAudioDetailSerializer(serializers.ModelSerializer):
    language=LanguageMiniSerializer()
    movie=serializers.StringRelatedField()

    class Meta:
        model=MovieAudio
        fields=['id','movie','language','name']