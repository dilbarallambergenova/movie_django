from rest_framework import serializers
from apps.movies.models import MovieSubtitle
from apps.movies.api_endpoints.language import LanguageMiniSerializer

class MovieSubtitleDetailSerializer(serializers.ModelSerializer):
    language=LanguageMiniSerializer()
    movie=serializers.StringRelatedField()

    class Meta:
        model=MovieSubtitle
        fields=['id','movie','language']