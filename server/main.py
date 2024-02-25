from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from server.routers import translations
from server.exceptions.handler import http_exception_handler

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://languagewire-ui.onrender.com"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"]
)

# Custom exception handler
app.add_exception_handler(HTTPException, http_exception_handler)

app.include_router(translations.router, prefix="/translations")
