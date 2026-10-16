# #fucntion to validtae the name
# def name_validation(name):
#     #to validate name as string
#     if not isinstance(name,str):
#         raise TypeError("Name must be a string") 
#     name=name.strip().lower().title()

#     #to validate the name field isn't blank
#     if not name:
#         raise ValueError("Name field can't be empty")

#     #to validate the boundary condition is met
#     if len(name)<3 or len(name)>50:
#         raise ValueError("Name field can't be less than 3 charcter or greater than 50")

#     return{
#         "name":name,
#         "valid":True
#     }

# def id_validation(emp_id):

#     #to validate the id field is an int
#     if isinstance(emp_id,bool):
#         raise ValueError("ID field can't be boolean")

#     if isinstance(emp_id,str):
#         emp_id=emp_id.strip()

#         try:
#             emp_id=int(emp_id)
#         except (ValueError,TypeError):
#             raise ValueError("Employee ID must be an integer field")

#     #to validate the boundary condition are met
#     if emp_id<1 or emp_id>100:
#         raise ValueError("Employee id must be between 1 to 100")

#     return{
#             "emp_id":emp_id,
#             "valid":True
#         }


def name_validation(name):
    try:

        name = name.strip().title()

        if not name:
            raise ValueError("Name field can't be empty")

        if not name.isalpha():
                raise ValueError("Name must contain only letters")
            # if not isinstance(name, str):
            #     raise TypeError("Name must be a string")

        if len(name) < 3 or len(name) > 50:
            raise ValueError(
                "Name field can't be less than 3 characters "
                "or greater than 50"
            )

        return {
            "name": name,
            "valid": True
        }

    except (ValueError, TypeError) as e:
        return {
            "error": str(e),
            "valid": False
        }


def id_validation(emp_id):
    try:
        if isinstance(emp_id, bool):
            raise ValueError("ID field can't be boolean")

        if isinstance(emp_id, str):
            emp_id = emp_id.strip()

            try:
                emp_id = int(emp_id)
            except ValueError:
                raise ValueError(
                    "Employee ID must be an integer field"
                )

        if not isinstance(emp_id, int):
            raise TypeError("Employee ID must be an integer")

        if emp_id < 1 or emp_id > 100:
            raise ValueError(
                "Employee ID must be between 1 and 100"
            )

        return {
            "emp_id": emp_id,
            "valid": True
        }

    except (ValueError, TypeError) as e:
        return {
            "error": str(e),
            "valid": False
        }

