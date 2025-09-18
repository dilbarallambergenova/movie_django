from rest_framework import serializers

from apps.meta.models import Comment


class CommentListSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields='__all__'
        