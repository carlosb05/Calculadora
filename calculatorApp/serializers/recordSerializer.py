from calculatorApp.models.record import Record
from rest_framework import serializers

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ['history', 'lastChangeDate', 'isActive']