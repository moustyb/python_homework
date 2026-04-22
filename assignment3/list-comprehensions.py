# TASK 3: List Comprehensions Practice
import csv
import os

# Read the CSV file into a list of lists
csv_path = os.path.join(os.path.dirname(__file__), "..", "csv", "employees.csv")
employees_data = []
with open(csv_path, "r", newline="") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        employees_data.append(row)

# List comprehension: create full names (skip header row)
# Assuming CSV structure: [first_name, last_name, ...]
full_names = [
    f"{row[0]} {row[1]}" 
    for row in employees_data[1:]  # Skip header
]
print("Full employee names:")
print(full_names)

# List comprehension: filter names containing letter "e" (case-insensitive)
names_with_e = [name for name in full_names if "e" in name.lower()]
print("\nNames containing 'e':")
print(names_with_e)
