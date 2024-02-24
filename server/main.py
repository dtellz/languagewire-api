from fastapi import FastAPI
from server.routers import translations

app = FastAPI()

app.include_router(translations.router, prefix="/translations")
