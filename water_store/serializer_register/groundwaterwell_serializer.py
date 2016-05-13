__author__ = 'anthonymendoza'

from rest_framework import serializers
from django.apps import apps


class GroundWaterWellSerializer(serializers.ModelSerializer):
    class Meta:
        model = apps.get_model("water_store", "GroundWaterWell")
        fields = ('id', 'site_name', 'site_code', 'latitude',
                  'longitude', 'county',
                  'date', 'value', 'units',
                  'active', 'source')
        read_only_fields = ['id']