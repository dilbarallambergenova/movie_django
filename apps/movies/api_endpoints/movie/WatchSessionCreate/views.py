from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status



from apps.movies.api_endpoints.movie.WatchSessionCreate.serializers import WatchSessionCreateSerializer
from apps.movies.models import WatchSession


class WatchSessionCreateView(APIView):
    def post(self,request,pk):
        serializer=WatchSessionCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
__all__=['WatchSessionCreateView']
        