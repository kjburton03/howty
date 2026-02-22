"""View module for handling requests for type data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rockapi.models import Location


class LocationView(ViewSet):
    """Rock API types view"""

    def list(self, request):
        """Handle GET requests to get all types

        Returns:
            Response -- JSON serialized list of types
        """

        locations = Location.objects.all()
        serialized = LocationSerializer(locations, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single type

        Returns:
            Response -- JSON serialized type record
        """

        item_location = Location.objects.get(pk=pk)
        serialized = LocationSerializer(item_location)
        return Response(serialized.data, status=status.HTTP_200_OK)


class LocationSerializer(serializers.ModelSerializer):
    """JSON serializer for types"""
    class Meta:
        model = Location
        fields = ('id', 'label', )