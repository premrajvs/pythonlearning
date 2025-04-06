# Scenario: Getting the current date and time and formatting it.
import datetime
now = datetime.datetime.now()
print(f"Current date and time: {now}")
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(f"Formatted date and time: {formatted_date}")