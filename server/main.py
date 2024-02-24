from fastapi import FastAPI, HTTPException
from server.routers import translations
from server.exceptions.handler import http_exception_handler

app = FastAPI()

# Custom exception handler
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(translations.router, prefix="/translations")
