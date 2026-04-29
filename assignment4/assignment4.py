import pandas as pd
import json
import os

print("="*60)
print("Starting Assignment 4 - Intro to Data Engineering")
print("="*60 + "\n")

# =============================================
# Task 1: Introduction to Pandas - Creating and Manipulating DataFrames
# =============================================

# 1. Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

task1_data_frame = pd.DataFrame(data)
print("Task 1.1 - DataFrame from dictionary:")
print(task1_data_frame)
print("\n" + "="*60 + "\n")

# 2. Add a new column - Salary
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("Task 1.2 - With Salary column:")
print(task1_with_salary)
print("\n" + "="*60 + "\n")

# 3. Modify Age column (increment by 1)
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("Task 1.3 - Age incremented:")
print(task1_older)
print("\n" + "="*60 + "\n")

# 4. Save to CSV without index
task1_older.to_csv('employees.csv', index=False)
print("Task 1.4 - employees.csv saved (no index)")

# =============================================
# Task 2: Loading Data from CSV and JSON
# =============================================

# 1. Read from CSV
task2_employees = pd.read_csv('employees.csv')
print("\nTask 2.1 - Loaded from employees.csv:")
print(task2_employees)
print("\n" + "="*60 + "\n")

# 2. Create and load additional_employees.json
additional_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open('additional_employees.json', 'w') as f:
    json.dump(additional_data, f, indent=2)

json_employees = pd.read_json('additional_employees.json')
print("Task 2.2 - Loaded from additional_employees.json:")
print(json_employees)
print("\n" + "="*60 + "\n")

# 3. Combine both DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Task 2.3 - Combined more_employees:")
print(more_employees)
print("\n" + "="*60 + "\n")

# =============================================
# Task 3: Data Inspection
# =============================================

# 1. head()
first_three = more_employees.head(3)
print("Task 3.1 - First three rows:")
print(first_three)
print("\n" + "="*60 + "\n")

# 2. tail()
last_two = more_employees.tail(2)
print("Task 3.2 - Last two rows:")
print(last_two)
print("\n" + "="*60 + "\n")

# 3. shape
employee_shape = more_employees.shape
print(f"Task 3.3 - Shape of more_employees: {employee_shape}")
print("\n" + "="*60 + "\n")

# 4. info()
print("Task 3.4 - DataFrame Info:")
more_employees.info()
print("\n" + "="*60 + "\n")

# =============================================
# Task 4: Data Cleaning  (Fixed to pass all tests)
# =============================================

print("Task 4 - Data Cleaning Started")
print("="*60)

# 1. Load dirty_data.csv
dirty_data = pd.read_csv('dirty_data.csv')
print("\nOriginal dirty_data:")
print(dirty_data)

clean_data = dirty_data.copy()

# 2. Remove duplicate rows
clean_data = clean_data.drop_duplicates()

# 3. Convert Age to numeric
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')

# 4. Clean Salary - replace placeholders and convert to numeric
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a', 'N/A'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')

# 5. Fill missing values: Age with mean, Salary with median
age_mean = clean_data['Age'].mean()
salary_median = clean_data['Salary'].median()

clean_data['Age'] = clean_data['Age'].fillna(age_mean)
clean_data['Salary'] = clean_data['Salary'].fillna(salary_median)

# 6. Convert Hire Date to datetime (Critical fix: use format='mixed')
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce', format='mixed')

# 7. Clean Name and Department
clean_data['Name'] = clean_data['Name'].str.strip()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("\nFinal Cleaned DataFrame:")
print(clean_data)
print("\n" + "="*60)

print("\n🎉 All tasks completed!")
print("Now run the test command:")
print("pytest -v -x assignment4-test.py")
