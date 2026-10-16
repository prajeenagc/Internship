from validation import *

name=input("Enter your name: ")
emp_id=input("Enter your Employee ID: ")
name_valid=name_validation(name)
id_valid=id_validation(emp_id)

print(name_valid,id_valid)

