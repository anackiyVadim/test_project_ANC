from rest_framework import serializers
from .models import Employee, Position


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    position = PositionSerializer()
    supervisor = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = '__all__'

    def get_supervisor(self, obj):
        if obj.supervisor:
            return {
                'id': obj.supervisor.id,
                'name': obj.supervisor.name,
                'surname': obj.supervisor.surname,
                'surname_patronymic': obj.supervisor.surname_patronymic,
                'data_admission': obj.supervisor.data_admission,
                'email': obj.supervisor.email,
                'position': obj.supervisor.position.position_name,
                'supervisor': obj.supervisor.supervisor.id if obj.supervisor.supervisor else None
            }
        return None