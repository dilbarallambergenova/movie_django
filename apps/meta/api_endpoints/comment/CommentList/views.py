from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.meta.models import Comment
from apps.meta.api_endpoints.comment.CommentList.serializers import CommentListSerializer

@api_view(['GET'])
def CommentListView(request):
    comments=Comment.objects.all()
    serializer=CommentListSerializer(comments,many=True)
    return Response(serializer.data)