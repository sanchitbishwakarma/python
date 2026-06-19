from datetime import datetime

str_time1 = "2026-06-19 08:15:00"
str_time2 = "2026-06-19 11:45:30"

# Parse strings into datetime objects matching the pattern
format_pattern = "%Y-%m-%d %H:%M:%S"
dt1 = datetime.strptime(str_time1, format_pattern)
dt2 = datetime.strptime(str_time2, format_pattern)

# Get the total minutes directly
minutes_diff = (dt2 - dt1).total_seconds() / 60
print(f"Difference in minutes: {minutes_diff}")
print(datetime.now().replace(microsecond=0))