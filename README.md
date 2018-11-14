# oncall

oncall is an app that manages employee oncall shifts (rosters)  and ensures
each shift worker has adequate time off and that shifts do not overlap or that
an employee does not start a shift back-to-back.

## Questions

1. Are breaks factored into the roster schedules? Or do emplyees take their
   allocated break when it suits?
2. What are the shift schedules per day? 7-3pm, 3pm-11pm, 11pm-7am? Does it
   matter? Do you need flexible schedules?
3. Do you need a minimum time between breaks or just a way to avoid
    back-to-back shifts?

## Assumptions

Some assumptions based on current requirements:

- Shifts start and end on the same day (//possibly extending into the night//)
- Employees are "free-form" and there is no integration into Identity providers

## Limitations

Currently the system does not support the following features at this time:

- Swapping shifts between employees (//e.g: an employee is sick//)
- Detecting shift conflicts such as Employees on holidays/leaves.
- Notifications and Reminders (//upcoming shifts, conflict warnings//)
- Schedule configuration (//e.g: week-long shifts, 2 days shifts, etc//)

These are considerations for future development.

## Building and Running

This assumes you have [Python 3](https://www.python.org/) already installed
as well as [virtualenvwrapepr](https://virtualenvwrapper.readthedocs.io/en/latest/).

If you don't you can easily set this up on macOS with [Homebrew](https://brew.sh):

```#!bash
$ brew install python
$ pip3 install virtualenvwrapper
$ source $(which virtualenvwrapper.sh)
```

Clone this repository:

```#!bash
$ git clone git@bitbucket.org:prologic/be_challenge.git
$ cd be_challenge
```

Create a virtual environment to manage dependencies:

```#!bash
$ mkvirtualenv -p python3 roster
```

Install dependencies:

```#!bash
pip install -r requirements.txt
```

Run the mgirations:

```#!bash
$ cd oncall
$ ./manage.py migrate
```

Run the development server:

```#!bash
$ ./manage.py runserver
```

## Running the Tests

There is also an included test suite which can be run with [py.test](https://docs.pytest.org/en/latest/):

```#!bash
$ py.test
```

## License

This work is licensed under the terms of the MIT License. See the `LICENSE`
file in this repository for details.
