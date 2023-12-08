import datetime

# Function to print results
def print_result(name, result):
    print(f"{name}: {result}")

# Get current date and time
current_datetime = datetime.datetime.now()
print_result("Current DateTime", current_datetime)

# Date Constructors
date1 = datetime.date(2022, 1, 15)
date2 = datetime.date.today()

# Time Constructors
time1 = datetime.time(12, 30, 45)
time2 = datetime.datetime.now().time()

# DateTime Constructors
datetime1 = datetime.datetime(2022, 1, 15, 12, 30, 45)
datetime2 = datetime.datetime.now()

# Date Methods
print_result("Date 1", date1)
print_result("Date 2", date2)
print_result("Date 1 Year", date1.year)
print_result("Date 1 Month", date1.month)
print_result("Date 1 Day", date1.day)

# Time Methods
print_result("Time 1", time1)
print_result("Time 2", time2)
print_result("Time 1 Hour", time1.hour)
print_result("Time 1 Minute", time1.minute)
print_result("Time 1 Second", time1.second)

# DateTime Methods
print_result("DateTime 1", datetime1)
print_result("DateTime 2", datetime2)
print_result("DateTime 1 Year", datetime1.year)
print_result("DateTime 1 Month", datetime1.month)
print_result("DateTime 1 Day", datetime1.day)
print_result("DateTime 1 Hour", datetime1.hour)
print_result("DateTime 1 Minute", datetime1.minute)
print_result("DateTime 1 Second", datetime1.second)

# Timedelta
delta = datetime.timedelta(days=5, hours=3)
new_datetime = datetime.datetime.now() + delta
print_result("New DateTime after Timedelta", new_datetime)
