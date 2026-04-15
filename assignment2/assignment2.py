import csv
import os
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
            stack_trace.append(f'File : {trace[0]}, Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")
        # Re-raise so pytest can see it if needed
        raise

employees = read_employees()   # This runs when the module is imported (required for tests)

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
    matches = list(filter(lambda row: int(row[employee_id_column]) == employee_id,
                          employees["rows"]))
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
                    rows.append(tuple(row))   # convert to tuple as required
        data['rows'] = rows
        return data

    minutes1 = read_one_csv('../csv/minutes1.csv')
    minutes2 = read_one_csv('../csv/minutes2.csv')
    return minutes1, minutes2

# Optional: demo calls (these run when you execute the file directly)
if __name__ == "__main__":
    print("Employees data loaded successfully.")
    print("First name of row 0:", first_name(0))
    print("Employee 1:", employee_find(1))
    print("Sorted by last_name (first 3):", sort_by_last_name()[:3])
    print("Employee dict example:", employee_dict(employees["rows"][0]))
    print("All employees as dict of dicts:", all_employees_dict())
    print("THISVALUE env var:", get_this_value())
    
    # Task 11 demo
    set_that_secret("new secret value!")
    print("Custom module secret:", custom_module.secret)
    
    # Task 12 demo
    m1, m2 = read_minutes()
    print("Minutes1 fields:", m1['fields'])
    print("Minutes2 rows count:", len(m2['rows']))
