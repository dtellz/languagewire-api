from fastapi import APIRouter, HTTPException, Query
from server.models.translations import TranslationQuery
from server.services.translations import TranslationService

router = APIRouter()

@router.get("/translate")
async def translate(
    text: str = Query(..., description="Text to translate"),
    lang: str = Query(..., description="Language to translate to")
):
    # Validate query params
    try:
        query = TranslationQuery(text=text, lang=lang)
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail={"error": "ValueError", "message": str(error)}
        )
    
    response = TranslationService.translate(query.lang)

    return {"translation": response}

@router.get("/jeringoza")
async def jeringoza(text: str = Query(..., description="Text to translate to Jeringoza")):
    # Validate query params
    try:
        input = JeringozaInput(value=text)
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail={"error": "ValueError", "message": str(error)}
        )
    return {"translation": TranslationService.jeringoza(input.value)}
