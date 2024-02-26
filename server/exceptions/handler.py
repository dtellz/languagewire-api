from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request: Request, exception: HTTPException) -> JSONResponse:
    # Check if this HTTPException was specifically raised due to a ValueError
    if isinstance(exception.detail, dict) and exception.detail.get("error") == "ValueError":
        # Custom formatting for ValueError-triggered HTTPException
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "status": "error",
                "statusCode": exception.status_code,
                "errorType": exception.detail.get("error"),
                "message": exception.detail.get("message"),
            }
        )
    else:
        # Default handling for other HTTPExceptions
        return JSONResponse(
            status_code=exception.status_code,
            content={
                "status": "error",
                "message": str(exception.detail)
            }
        )
