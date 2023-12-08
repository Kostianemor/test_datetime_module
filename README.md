# test_modules
- [datetime](#datetime Module Functions and Methods)
- [time](#getting-started)

## datetime Module Functions and Methods

1. **datetime.datetime.now()**: Returns the current local date and time.

2. **datetime.date(year, month, day)**: Returns a date object with the specified year, month, and day.

3. **datetime.time(hour, minute, second, microsecond)**: Returns a time object with the specified hour, minute, second, and microsecond.

4. **datetime.datetime(year, month, day, hour, minute, second, microsecond)**: Returns a datetime object with the specified year, month, day, hour, minute, second, and microsecond.

5. **datetime.date.today()**: Returns the current local date.

6. **datetime.datetime.now().time()**: Returns the current local time.

7. **datetime.timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])**: Represents the difference between two dates or times.

8. **date.year, date.month, date.day**: Attributes of a date object.

9. **time.hour, time.minute, time.second**: Attributes of a time object.

10. **datetime.year, datetime.month, datetime.day, datetime.hour, datetime.minute, datetime.second**: Attributes of a datetime object.

## time Module Functions and Methods

1. **time.time()**: Returns the current time in seconds since the epoch (January 1, 1970).

2. **time.localtime([secs])**: Returns the local time in a struct_time format or a time.struct_time object.

3. **time.strftime(format[, t])**: Returns a string representing a time according to the format string.

4. **time.sleep(secs)**: Suspends execution for the given number of seconds.

5. **time.gmtime([secs])**: Converts a time expressed in seconds since the epoch to a struct_time in UTC.

6. **time.daylight**: Returns nonzero if a DST timezone is defined.

7. **time.clock()**: Returns the current processor time as a floating-point number expressed in seconds.

