"""
DAILY ACTIVITY TRACKER
Asks what you did in each time slot of the day (1 hour, 2 hours or
30 minutes), then prints a summary and saves it to activity_log.txt.

Author: Vicky
"""
from datetime import datetime


def label(minutes):
    """Turn minutes since midnight into a 12-hour time like '1:30 PM'."""
    h = (minutes // 60) % 24
    m = minutes % 60
    suffix = "AM" if h < 12 else "PM"
    h12 = h % 12
    if h12 == 0:
        h12 = 12
    return f"{h12}:{m:02d} {suffix}"


n = input("select time interval to track your activities:\n1 for 1hrs\n2 for 2hrs\n3 for 30mins\n").strip()
if n == "1":
    step = 60
elif n == "2":
    step = 120
elif n == "3":
    step = 30
else:
    print("INVALID CHOICE, using 1 hour")
    step = 60

log = []
for start in range(0, 24 * 60, step):
    end = start + step
    t1 = input(f"what you did at {label(start)} to {label(end)}: ")   # fixed: input() takes one string
    log.append((label(start), label(end), t1))

print("\nYOUR DAY AT A GLANCE")
print("-" * 45)
for a, b, work in log:
    print(f"{a:>9} - {b:<9} | {work}")

with open("activity_log.txt", "a") as f:
    f.write("\n=== " + datetime.now().strftime("%d/%m/%Y %I:%M %p") + " ===\n")
    for a, b, work in log:
        f.write(f"{a} - {b} : {work}\n")
print("\nSaved to activity_log.txt")
