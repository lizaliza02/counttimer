import datetime

# Get the current date and time
current_time = datetime.datetime.now()

# Format the current time as a string
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

# Print the formatted time
print(formatted_time)


import time

print("~~~~THE COUNTDOWN TIMER~~~~")
# this is a simple input function.
my_time = int(input("Enter the time in seconds:"))

for x in range(my_time, 0, -1):
    seconds = x % 60
    minutes = int(x/60) % 60
    hours = int(x/3600) % 24
    print(f"{hours:02}:{minutes:02}:{seconds:02}")
    time.sleep(1)

print("Time is up!")
