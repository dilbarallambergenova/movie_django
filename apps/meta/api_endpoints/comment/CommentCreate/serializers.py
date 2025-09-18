from rest_framework import serializers
from apps.meta.models import Comment

class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"