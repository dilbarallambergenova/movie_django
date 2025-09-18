from rest_framework.views import APIView
from rest_framework.response import Response

from apps.meta.api_endpoints.comment.CommentCreate.serializers import CommentCreateSerializer


class CommentCreateView(APIView):
    def post(self,request):
        serializer=CommentCreateSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
        return Response({'status':'ok'})
