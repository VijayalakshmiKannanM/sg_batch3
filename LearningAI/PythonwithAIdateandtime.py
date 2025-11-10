# datetime_demo.py
"""
Date & Time operations demo:
- Get current date/time
- Formatting & parsing (strftime / strptime)
- Time arithmetic with timedelta
- Timezones (zoneinfo) and conversions
- UNIX timestamps and ISO formats
- Measuring elapsed time
- Iterating dates (range of dates)
- Optional: using dateutil for advanced ops (commented)
"""

from datetime import datetime, date, time, timedelta
from zoneinfo import ZoneInfo   # Python 3.9+
import time as time_module

# ---------------- Current date & time ----------------
now = datetime.now()
utc_now = datetime.utcnow()
print("Current local datetime:", now)
print("Current UTC datetime (naive):", utc_now)

# ---------------- Formatting ----------------
print("\n--- Formatting ---")
fmt1 = now.strftime("%Y-%m-%d %H:%M:%S")
fmt2 = now.strftime("%A, %d %B %Y %I:%M %p")
print("ISO-like format:", fmt1)
print("Readable:", fmt2)

# ---------------- Parsing from string ----------------
print("\n--- Parsing ---")
s = "2025-11-08 06:30:15"
parsed = datetime.strptime(s, "%Y-%m-%d %H:%M:%S")
print("Parsed:", parsed, type(parsed))

# ---------------- Time arithmetic ----------------
print("\n--- Arithmetic (timedelta) ---")
delta = timedelta(days=7, hours=3, minutes=30)
future = now + delta
past = now - timedelta(days=30)
print("7 days and 3.5 hours from now:", future)
print("30 days ago:", past)

# ---------------- Timezone-aware datetimes ----------------
print("\n--- Timezones (zoneinfo) ---")
# make timezone-aware datetime from naive 'now'
local_tz = ZoneInfo("Asia/Kolkata")    # user's timezone example
aware_local = now.replace(tzinfo=local_tz)
aware_utc = aware_local.astimezone(ZoneInfo("UTC"))
print("Aware local (Asia/Kolkata):", aware_local)
print("Converted to UTC:", aware_utc)

# convert between two zones
ny = aware_local.astimezone(ZoneInfo("America/New_York"))
print("Local -> New York:", ny)

# ---------------- UNIX timestamp ----------------
print("\n--- UNIX timestamp ---")
ts = now.timestamp()
print("UNIX timestamp (seconds):", ts)
print("Back from timestamp:", datetime.fromtimestamp(ts))

# ---------------- ISO formats ----------------
print("\n--- ISO formats ---")
print("ISO 8601 (now):", now.isoformat())
print("ISO date:", date.today().isoformat())

# ---------------- Measure elapsed time ----------------
print("\n--- Measure elapsed time ---")
t0 = time_module.perf_counter()
# some work: simple loop
total = sum(i*i for i in range(100000))
t1 = time_module.perf_counter()
print(f"Work result (sum of squares): {total}, elapsed: {t1 - t0:.6f} seconds")

# ---------------- Iterating dates (range) ----------------
print("\n--- Iterate dates ---")
start = date.today()
days = [start + timedelta(days=i) for i in range(7)]
print("Next 7 dates:")
for d in days:
    print(" ", d.isoformat(), d.strftime("%a"))

# ---------------- Next weekday example ----------------
def next_weekday(given: date, weekday: int) -> date:
    """Return the next date >= given which is the given weekday (0=Mon .. 6=Sun)."""
    days_ahead = (weekday - given.weekday() + 7) % 7
    return given + timedelta(days=days_ahead)

today = date.today()
next_monday = next_weekday(today, 0)  # 0 = Monday
print("\nNext Monday on or after today:", next_monday)

# ---------------- Advanced: adding months (note) ----------------
print("\n--- Note: adding months ---")
print("Adding months isn't in stdlib. For robust month arithmetic use 'dateutil.relativedelta'.")
print("Example (if you have dateutil):")
print("    from dateutil.relativedelta import relativedelta")
print("    new = date.today() + relativedelta(months=+1)")

# End
print("\nDemo finished.")
