from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from api.models import DataModel
from api.serializers import DataSerializer


# Create your views here.


class APIDataView(APIView):
    def get(self, request):
        try:
            dm = DataModel.objects.get(player=request.user)
            serializer = DataSerializer(dm)
            return Response(serializer.data)
        except DataModel.DoesNotExist:
            return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        try:
            dm = DataModel.objects.get(player=request.user)
        except DataModel.DoesNotExist:
            dm = DataModel()
            dm.player = request.user
        serializer = DataSerializer(dm, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

