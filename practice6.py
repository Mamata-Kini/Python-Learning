rollnum_set ={101,102,103,105,101,108,107,102}
print(rollnum_set)

emp_list = [
                    (101, "Alice", 5000),
                    (102, "Bosco", 3000),
                    (103, "Crish", 4000)
    
]

print(emp_list, type(emp_list))

emp_id = int(input("Enter employee Id"))
if any(emp[0] == emp_id for emp in emp_list):
    print("Employee found")
else:
    print("Employee not found")