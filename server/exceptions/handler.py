from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

async def http_exception_handler(request: Request, exc: HTTPException):
    # Check if this HTTPException was specifically raised due to a ValueError
    if isinstance(exc.detail, dict) and exc.detail.get("error") == "ValueError":
        # Custom formatting for ValueError-triggered HTTPException
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "statusCode": exc.status_code,
                "errorType": exc.detail.get("error"),
                "message": exc.detail.get("message"),
            }
        )
    else:
        # Default handling for other HTTPExceptions
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "status": "error",
                "message": str(exc.detail)
            }
        )
