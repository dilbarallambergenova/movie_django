from rest_framework import serializers

from apps.movies.models import MovieFile
from apps.movies.api_endpoints.language import LanguageMiniSerializer

class MovieFileDetailSerializer(serializers.ModelSerializer):
    language=LanguageMiniSerializer()
    movie=serializers.StringRelatedField()

    class Meta:
        model=MovieFile
        fields=['id','language','movie','quality','file']