from validation import *

try:
    empid=input("PLease enter your valid Employee ID: ")
    ans=id_valid(empid)
    print(ans)

except ValueError as e:
    print(f"Invalid ID: {e}")


