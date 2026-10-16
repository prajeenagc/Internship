# Rules
# 1. Check whether both name and employee-id field are string and integer respectively.
# 2. if name field is integer throw an error
# 3. if employee id field is string convert it to int if possible else throw error
# 4. check for and remove whitespace.
# 5. capitalize the title words.
# 6. reject blank title or employee id.
# 7. reject title shorter than 3 charactersor longer than 50
# 8. reject employee-id if it's less than 1 or greater than 100
# 9. return clean data and if it's valid

def validation(name,employee_id):

    if not isinstance(name,str):
        raise TypeError("Name must be a string")
    name=name.strip().title()
    

    if not name:
        raise ValueError("Name cannot be blank")

    if len(name)<3 or len(name)>50:
        raise ValueError("Name must be in between 3 and 50 characters")

    if isinstance(employee_id,bool):
        raise TypeError("Employee ID must be an integer")

    if isinstance(employee_id,str):
        employee_id=employee_id.strip()

        if not employee_id:
            raise ValueError("Employee ID cannot be blank")
    try:
        employee_id=int(employee_id)
    except (ValueError,TypeError):
        raise ValueError("Employee ID must be valid integer")

    if employee_id<1 or employee_id>100:
        raise ValueError("Employee ID must be between the range 1 to 100")

    return{
        "name":name,
        "employee_id":employee_id,
        "valid":True

    }

name = input("Enter your name: ")
employee_id = input("Enter your employee ID: ")

try:
    result = validation(name, employee_id)
    print(result)
except (ValueError, TypeError) as error:
    print("Invalid:", error)

        

        
        
        








