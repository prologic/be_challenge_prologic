# Schema Design

The schema for the oncall roster app is currently comprised of two models:

- `Employee` -- This holds the first and last name of each employee
- `Shift`    -- This holds a row per shift with a reference to the employee
                for that shift as well as the start and end date and time.

## Example(s)

### Creating records:

```#!python
>>> from roster.models import Employee, Shift
>>> e1 = Employee(firstname="James", lastname="Mills")
>>> e1.save()
>>> from django.utils import timezone
>>> from datetime import timedelta
>>> s1 = Shift(employee=e1, start=timezone.now(), end=(timezone.now() + timedelta(days=7)))
>>> s1.save()
```

### Querying records:

```#!python
>>> from roster.models import Employee, Shift
>>> Employee.objects.all()
<QuerySet [<Employee: Employee (James Mills)>]>
>>> Shift.objects.all()
<QuerySet [<Shift: Shift(for Employee (James Mills) starting on 2018-11-14 07:45:33.249819+00:00 for 7 days, 0:00:00.000016 ending on 2018-11-21 07:45:33.249835+00:00)>]>
```
