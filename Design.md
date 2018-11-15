# Design Notes

NB: The point of this exercise (//I assume//) is to demonstrate a level of
competency in Python, Django, Micro-services, API design, Data Structures, etc.

I have to tress that in the ~2 or so hours I spent on this I wasn't able to
get as much done as I had originally hoped. This is mainly due to not having
used Django in some years (~3 or so, Facebook doesn't use Django!)

That being said; I am quite confident given more time I could completely write
a high quality backend for this Roster oncall application suitable for a
Frontend Engineer to write a swank React/React-native UI for! Given even more
time I could write a Bootstrap or Spectre+Umbrella UI for as well.

Some thinking I was doing at the time but sadly have to stop at this stage
as I'm in the middle of packing boxes, moving and driving down to Brisbane!

## Allocation of Shifts

This is arguably the most interesting part of the problem so I'll attempt to
design an algorithm in pseudo-code that I believe solve the problem.

Assuming we create an API endpoint called `/allocate/?shifts=<int>&length=<int>`
(//at this stage we assume there is only a single roster, but this could be
generalized to support other named roster, i.e: multi-use//), then an
algorithm that takes a list of employees and allocates each employee to an
appropriate shift might look like the following:

```#!python
def allocate(self, request, shifts, length):
   """allocates shifts for up to `shifts` with each shift duration of `length`
   ensuring each employee has adequate break between shifts and therefore
   has no break--back shifts
   """

   time_between_shifts = 10  # 10 hours break between shifts

   shifts = defaultdict(list)  # [{"employee_1": [(shit_1_start, shift_1_end), ...], ...}
   start_date = datetime.now()
   end_date = datetime.now() + timedelta(hours=length)  # assume length in hours
   all_employees = get_all_employees()
   for _ in range(shifts):
       employees = shuffle(all_employees[:])  # duplicate the list and randomize
       while employees:
           employee = employees.pop()
           current_shifts = shifts.get(employee, [])
           if not current_shifts or (
               current_shifts and ((current_shifts[-1][1] - end_date) >= time_between_shifts)
           ):
               shifts[employee].append((start_date, end_date)]
               start_date, end_date = end_date, (end_date + timedelta(hours=length)
               continue
           employees.insert(0, employee)  # insert to left of list
```

Basically in English, for n shift allocations of length y, assign a random
employee to the next shift if they have a time delta of the minimum break
period between shifts.
