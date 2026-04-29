import pandas as pd
import json
import os

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
print("Task 1 - Original DataFrame:")
print(task1_data_frame)
print("\n" + "="*50 + "\n")

# 2. Add a new column (Salary)
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print("Task 1 - With Salary:")
print(task1_with_salary)
print("\n" + "="*50 + "\n")

# 3. Modify an existing column (increment Age)
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print("Task 1 - Older Employees:")
print(task1_older)
print("\n" + "="*50 + "\n")

# 4. Save the DataFrame as CSV (no index)
task1_older.to_csv('employees.csv', index=False)
print("employees.csv saved successfully (without index).")
print("Contents of employees.csv:")
with open('employees.csv', 'r') as f:
    print(f.read())
print("\n" + "="*50 + "\n")

# =============================================
# Task 2: Loading Data from CSV and JSON
# =============================================

# 1. Read data from CSV
task2_employees = pd.read_csv('employees.csv')
print("Task 2 - Loaded from employees.csv:")
print(task2_employees)
print("\n" + "="*50 + "\n")

# 2. Create additional_employees.json
additional_data = [
    {"Name": "Eve", "Age": 28, "City": "Miami", "Salary": 60000},
    {"Name": "Frank", "Age": 40, "City": "Seattle", "Salary": 95000}
]

with open('additional_employees.json', 'w') as f:
    json.dump(additional_data, f, indent=2)

print("additional_employees.json created.")

# Load the JSON file
json_employees = pd.read_json('additional_employees.json')
print("\nTask 2 - Loaded from JSON:")
print(json_employees)
print("\n" + "="*50 + "\n")

# 3. Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print("Task 2 - Combined DataFrame (more_employees):")
print(more_employees)
print("\n" + "="*50 + "\n")

# =============================================
# Task 3: Data Inspection
# =============================================

# 1. head()
first_three = more_employees.head(3)
print("Task 3 - First three rows:")
print(first_three)
print("\n" + "="*50 + "\n")

# 2. tail()
last_two = more_employees.tail(2)
print("Task 3 - Last two rows:")
print(last_two)
print("\n" + "="*50 + "\n")

# 3. shape
employee_shape = more_employees.shape
print(f"Task 3 - Shape of more_employees: {employee_shape}")
print("\n" + "="*50 + "\n")

# 4. info()
print("Task 3 - DataFrame Info:")
more_employees.info()
print("\n" + "="*50 + "\n")

# =============================================
# Task 4: Data Cleaning
# =============================================

# 1. Load dirty_data.csv
dirty_data = pd.read_csv('dirty_data.csv')
print("Task 4 - Original dirty_data:")
print(dirty_data)
print("\n" + "="*50 + "\n")

clean_data = dirty_data.copy()

# 2. Remove duplicate rows
clean_data = clean_data.drop_duplicates()
print("After removing duplicates:")
print(clean_data)
print("\n" + "="*50 + "\n")

# 3. Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print("After converting Age to numeric:")
print(clean_data)
print("\n" + "="*50 + "\n")

# 4. Convert Salary to numeric and replace placeholders with NaN
clean_data['Salary'] = clean_data['Salary'].replace(['unknown', 'n/a', 'N/A'], pd.NA)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors='coerce')
print("After cleaning Salary column:")
print(clean_data)
print("\n" + "="*50 + "\n")

# 5. Fill missing numeric values
age_mean = clean_data['Age'].mean()
salary_median = clean_data['Salary'].median()

clean_data['Age'] = clean_data['Age'].fillna(age_mean)
clean_data['Salary'] = clean_data['Salary'].fillna(salary_median)

print("After filling missing values (Age=mean, Salary=median):")
print(clean_data)
print("\n" + "="*50 + "\n")

# 6. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print("After converting Hire Date to datetime:")
print(clean_data)
print("\n" + "="*50 + "\n")

# 7. Strip whitespace and standardize Name & Department to uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()

print("Final cleaned DataFrame:")
print(clean_data)
print("\n" + "="*50 + "\n")

print("All tasks completed! Run the tests now:")
print("pytest -v -x assignment4-test.py")
