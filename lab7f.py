#!/usr/bin/env python3
# Student ID: kartik

class Time:
    """Simple object type for time of the day.
        data attributes: hour, minute, second
        function attributes: __init__, __str__, __repr__, __add__,
                             time_to_sec, format_time,
                             change_time, sum_time
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self):
        """Return a string representation for the object self"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """Return a string representation for the object self with '.' as delimiter"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload the '+' operator to add two time objects"""
        return self.sum_times(t2)

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two time objects and return the sum as a new Time object."""
        total_seconds = self.time_to_sec() + t2.time_to_sec()
        return sec_to_time(total_seconds)

    def change_time(self, seconds):
        """Change the time by a given number of seconds."""
        time_seconds = self.time_to_sec()
        nt = sec_to_time(time_seconds + seconds)
        self.hour, self.minute, self.second = nt.hour, nt.minute, nt.second

    def time_to_sec(self):
        """Convert a time object to seconds since midnight"""
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def valid_time(self):
        """Validate the time object's attributes"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.minute >= 60 or self.second >= 60 or self.hour >= 24:
            return False
        return True


def sec_to_time(seconds):
    """Convert seconds since midnight into a Time object"""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
