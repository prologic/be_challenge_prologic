from django.db import models


class Employee(models.Model):
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)

    def __str__(self):
        return "Employee ({} {})".format(self.firstname, self.lastname)


class Shift(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return "Shift(for {} starting on {} for {} ending on {})".format(
            self.employee,
            self.start,
            (self.end - self.start),
            self.end,
        )
