# Scenario (reading): Reading data from a CSV file.
import csv
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
# (Assume 'data.csv' exists with comma-separated values)

# Scenario (writing): Writing data to a CSV file.
data_to_write = [["Name", "Age", "City"], ["Bob", 25, "Chicago"], ["Charlie", 32, "Seattle"]]
with open("output.csv", "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data_to_write)