from django.http import HttpResponse, Http404
from rest_framework import views, viewsets
from rest_framework.response import Response

from .models import Employee, Shift
from .serializers import EmployeeSerializer, ShiftSerializer


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def view_shift(request, shift_id):
    return HttpResponse("You're looking at shift %s." % shift_id)


def upcoming_shifts(request, employee_id):
    response = "You're looking at upcoming shifts for %s"
    return HttpResponse(response % employee_id)


def add_shift(request):
    return HttpResponse("You're looking at adding a new shift")


class EmployeeDetail(views.APIView):

    def get_object(self, id):
        try:
            return Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)


class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or added
    """

    queryset = Employee.objects.all().order_by("lastname")
    serializer_class = EmployeeSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows shifts to be viewed or edited.
    """

    queryset = Shift.objects.all()
    serializer_class = ShiftSerializer
