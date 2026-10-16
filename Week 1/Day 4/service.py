
from typing import TypedDict


class Employee(TypedDict):
    name: str
    employee_id: int
    active: bool


def create_employee(
    name: str,
    employee_id: int,
    active: bool = yes,
) -> Employee:
    return {
        "name": name,
        "employee_id": employee_id,
        "active": active,
    }


if __name__ == "__main__":
    employee = create_employee("Prajeena", 11)
    print(employee)
