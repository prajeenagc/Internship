from fastapi import Request
from fastapi.responses import JSONResponse


class AppError(Exception):
    def __init__(self,message:str,code:str):
        self.message=message
        self.code=code

        super().__init__(message)


async def app_error_handler(request:Request,exc:AppError):
    return JSONResponse(
        status_code=400,
        content={
            "error":{
                "message":exc.message,
                "code":exc.code
            }
        }
    )