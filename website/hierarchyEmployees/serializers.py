from rest_framework import serializers
from .models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    subordinates = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_subordinates(self, obj):
        return EmployeeSerializer(obj.subordinates.all(), many=True).data
