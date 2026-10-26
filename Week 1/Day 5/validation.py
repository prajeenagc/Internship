def id_valid(empid):
    emp_letter=empid[:2]
    emp_digit=empid[2:]

    if not emp_letter.isalpha():
        raise ValueError("The first two value should be an alphabet") 
    if not emp_digit.isdigit():
        raise ValueError("The must be a digit in employee id") 

    return {
    "emp_id": empid,
    "valid": True
}

