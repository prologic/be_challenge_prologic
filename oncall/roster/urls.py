from django.urls import path
from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"employees", views.EmployeeViewSet)
router.register(r"shifts", views.ShiftViewSet)

print("###")
for x in router.urls:
    print(repr(x))
print("###")

app_name = "roster"

urlpatterns = [
    path("", views.index, name="index"),

    path("shift/<int:shift_id>/", views.view_shift, name="view_shift"),
    path("upcoming/<int:employee_id>/", views.upcoming_shifts, name="upcoming_shifts"),
    path("add/", views.add_shift, name="add"),

    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
