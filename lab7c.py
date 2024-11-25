#!/usr/bin/env python3
# Student ID: kartik

class Time:
    """Simple object type for time of the day.
    Data attributes: hour, minute, second.
    """
    def __init__(self, hour=0, minute=0, second=0):
        """Constructor for time object."""
        self.hour = hour
        self.minute = minute
        self.second = second

def format_time(t):
    """Return time object (t) as a formatted string."""
    return f'{t.hour:02d}:{t.minute:02d}:{t.second:02d}'

def valid_time(t):
    """Check if the time object attributes are valid."""
    if t.hour < 0 or t.minute < 0 or t.second < 0:
        return False
    if t.hour >= 24 or t.minute >= 60 or t.second >= 60:
        return False
    return True

def time_to_sec(time):
    """Convert a time object to an integer representing seconds since midnight."""
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds

def sec_to_time(seconds):
    """Convert an integer of seconds since midnight to a time object."""
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

def sum_times(t1, t2):
    """Add two time objects using seconds-based conversion."""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    total_seconds %= 24 * 60 * 60
    return sec_to_time(total_seconds)

def change_time(time, seconds):
    """Modify a time object by adding/subtracting seconds using seconds-based conversion."""
    total_seconds = time_to_sec(time) + seconds
    total_seconds %= 24 * 60 * 60
    modified_time = sec_to_time(total_seconds)
    time.hour = modified_time.hour
    time.minute = modified_time.minute
    time.second = modified_time.second
    return None
