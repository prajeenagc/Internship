from strawberry import ID
from . import schemas
from typing import Any, List

class QueryResolver:
    @staticmethod
    def get_tasks(pagination: Any) -> List[schemas.Task]: # pyright: ignore[reportReturnType]
        pass

    @staticmethod
    def get_task(task_id:ID)->(schemas.Task|None):
        pass

    class MutationResolver:
        @staticmethod
        def add_task(task_content: str) -> schemas.Task:# pyright: ignore[reportReturnType]
            pass

        @staticmethod
        def update_task(task_id: ID, task:Any) -> (schemas.Task|None):
            pass

        @staticmethod
        def delete_task(task_id:ID) -> None:
            pass