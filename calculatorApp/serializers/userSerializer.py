from rest_framework import serializers
from calculatorApp.models.user import User
from calculatorApp.models.record import Record
from calculatorApp.serializers.recordSerializer import RecordSerializer

class UserSerializer(serializers.ModelSerializer):
    record = RecordSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'record']
    def create(self, validated_data):
        recordData = validated_data.pop('record')
        userInstance = User.objects.create(**validated_data)
        Record.objects.create(user=userInstance, **recordData)
return userInstance
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        record = Record.objects.get(user=obj.id)
        return {
                    'id': user.id,
                    'username': user.username,
                    'name': user.name,
                    'email': user.email,
                    'record': {
                        'id': record.id,
                        'history': record.history,
                        'lastChangeDate': record.lastChangeDate,
                        'isActive': account.isActive
                    }       
        }