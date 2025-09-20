from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from apps.meta.models import Comment
from apps.meta.api_endpoints.comment.CommentList.serializers import CommentListSerializer

@api_view(['GET'])
def CommentListView(request,pk):
    comments=Comment.objects.filter(movie_id=pk)
    serializer=CommentListSerializer(comments,many=True)
    return Response(serializer.data)