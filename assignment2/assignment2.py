import csv
import os
from datetime import datetime
import custom_module

# ===================== TASK 2 =====================
def read_employees():
    employees = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    employees['fields'] = row
                else:
                    rows.append(row)
        employees['rows'] = rows
        return employees
    except Exception as e:
        import traceback
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        raise

employees = read_employees()   # global variable required for tests

# ===================== TASK 3 =====================
def column_index(col_name):
    return employees["fields"].index(col_name)

employee_id_column = column_index("employee_id")

# ===================== TASK 4 =====================
def first_name(row_num):
    col_idx = column_index("first_name")
    return employees["rows"][row_num][col_idx]

# ===================== TASK 5 =====================
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees["rows"]))
    return matches

# ===================== TASK 6 =====================
def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

# ===================== TASK 7 =====================
def sort_by_last_name():
    last_name_idx = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_idx])
    return employees["rows"]

# ===================== TASK 8 =====================
def employee_dict(row):
    emp_dict = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            emp_dict[field] = row[i]
    return emp_dict

# ===================== TASK 9 =====================
def all_employees_dict():
    all_dict = {}
    id_idx = column_index("employee_id")
    for row in employees["rows"]:
        emp_id = row[id_idx]
        all_dict[emp_id] = employee_dict(row)
    return all_dict

# ===================== TASK 10 =====================
def get_this_value():
    return os.getenv('THISVALUE')

# ===================== TASK 11 =====================
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

# ===================== TASK 12 =====================
def read_minutes():
    def read_one_csv(filename):
        data = {}
        rows = []
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    data['fields'] = row
                else:
                    rows.append(tuple(row))   # must be tuple for set
        data['rows'] = rows
        return data

    minutes1 = read_one_csv('../csv/minutes1.csv')
    minutes2 = read_one_csv('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()   # global variables

# ===================== TASK 13 =====================
def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2)

minutes_set = create_minutes_set()

# ===================== TASK 14 =====================
def create_minutes_list():
    minutes_list = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

minutes_list = create_minutes_list()

# ===================== TASK 15 =====================
def write_sorted_list():
    # Sort by datetime (second element of tuple)
    minutes_list.sort(key=lambda x: x[1])
    
    # Convert datetime back to string for CSV
    sorted_data = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))
    
    # Write to minutes.csv
    with open('./minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])          # header row
        writer.writerows(sorted_data)
    
    return sorted_data

# Run this function so the file gets created
write_sorted_list()

# Optional: print statements so you can see it works when you run the file
if __name__ == "__main__":
    print("✅ Assignment 2 loaded successfully!")
    print("First employee name:", first_name(0))
    print("THISVALUE:", get_this_value())
