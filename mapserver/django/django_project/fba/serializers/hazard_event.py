import json
from rest_framework import serializers
from rest_framework_gis.serializers import (
    GeoFeatureModelSerializer, GeometrySerializerMethodField)
from fba.models.all import HazardEvent, HazardMap, HazardType


class HazardEventSerializer(serializers.ModelSerializer):
    """
    Serializer for hazard event model.
    """
    hazard_map = serializers.SerializerMethodField()
    hazard_type = serializers.SerializerMethodField()

    def get_hazard_type(self, obj):
        try:
            hazard_type = HazardType.objects.get(
                id=obj.hazard_type_id
            )
            return hazard_type.name
        except HazardType.DoesNotExist:
            return '-'

    def get_hazard_map(self, obj):
        try:
            hazard_map = HazardMap.objects.get(
                id=obj.flood_map_id
            )
            return HazardMapSerializer(hazard_map).data
        except HazardMap.DoesNotExist:
            return '-'

    class Meta:
        model = HazardEvent
        fields = (
            'source',
            'notes',
            'forecast_date',
            'acquisition_date',
            'link',
            'hazard_type',
            'trigger_status',
            'hazard_map'
        )


class HazardMapSerializer(serializers.ModelSerializer):
    """
    Serializer for hazard map model
    """
    class Meta:
        model = HazardMap
        fields = (
            'notes',
            'place_name'
        )
