from dataclasses import field
from rest_framework import serializers
from . models import foodstuff

class foodstuffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = foodstuff
        fields = ('Mfd_id', 'Name', 'UnitPrice', 'UnitsInStock')