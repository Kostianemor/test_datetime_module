import time

# Function to print results
def print_result(name, result):
    print(f"{name}: {result}")

# Time Functions
timestamp = time.time()
print_result("Current Timestamp", timestamp)

local_time = time.localtime()
print_result("Local Time", local_time)

formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print_result("Formatted Local Time", formatted_time)

# Sleep for 2 seconds
print("Sleeping for 2 seconds...")
time.sleep(2)
print_result("After Sleep", "Woke up!")

# Time Methods
print_result("Current UTC Time", time.gmtime())
print_result("Daylight Saving Time", time.daylight != 0)

# Clock Function (CPU time since process start)
start_time = time.clock()
# Simulate some processing time
for _ in range(1000000):
    _ = _ * _
end_time = time.clock()
print_result("CPU Time Elapsed", end_time - start_time)
