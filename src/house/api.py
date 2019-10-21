from rest_framework import viewsets
from rest_framework.response import Response

from house.models import House
from house.serializers import CustomPagination, HouseSerializer, HouseDataSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    pagination_class = CustomPagination
    serializer_class = HouseSerializer
    lookup_field = 'slug'

    # Only for custom validations
    def create(self, request, *args, **kwargs):
        serializer = HouseDataSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
