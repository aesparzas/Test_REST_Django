from decimal import Decimal

from django.core.validators import MinValueValidator
from rest_framework import pagination, serializers
from rest_framework.response import Response

from house.models import House


class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, data):
        response = {
            "user": self.request.user.id if self.request.user else 'Unknown',
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'products': data,
        }
        return Response(response)


class HouseSerializer(serializers.ModelSerializer):

    class Meta:
        model = House
        fields = House.editable_fields() + ['slug']
        lookup_field = 'slug'


class HouseDataSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=50)
    address = serializers.CharField(required=True, max_length=100)
    surface = serializers.IntegerField(required=True, validators=[MinValueValidator(Decimal('0.01'))])
    contact_email = serializers.EmailField(required=True)

    def save(self, **kwargs):
        return House.objects.create(**self.validated_data)

    def validate_name(self, value):
        if House.objects.filter(name=value).exists():
            raise serializers.ValidationError('Ya existe una propiedad con ese nombre')
        return value
