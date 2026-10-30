import logging
import time
import uuid

from fastapi import Request

logger = logging.getLogger(__name__)


async def request_middleware(request: Request, call_next):
    request_id = str(uuid.uuid4())

    request.state.request_id = request_id

    start_time = time.perf_counter()

    response = await call_next(request)

    duration = time.perf_counter() - start_time

    response.headers["X-Request-ID"] = request_id

    logger.info(
        "request_id=%s method=%s path=%s status=%s duration=%.4fs",
        request_id,
        request.method,
        request.url.path,
        response.status_code,
        duration
    )

    return response