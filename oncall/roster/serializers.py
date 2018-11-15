from rest_framework import serializers

from .models import Employee, Shift


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Employee
        fields = ("firstname", "lastname")


class ShiftSerializer(serializers.HyperlinkedModelSerializer):

    employee = serializers.HyperlinkedRelatedField(
        many=True,
        queryset=Employee.objects.all(),
        view_name="employee-detail",
    )

    class Meta:
        model = Shift
        fields = ("employee", "start", "end")
