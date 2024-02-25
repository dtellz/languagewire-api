from fastapi import APIRouter, HTTPException, Query
from server.models.translations import TranslationQuery, jeringonzaInput
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

@router.get("/jeringonza")
async def jeringonza(text: str = Query(..., description="Text to translate to jeringonza")):
    # Validate query params
    try:
        input = jeringonzaInput(value=text)
    except ValueError as error:
        raise HTTPException(
            status_code=422,
            detail={"error": "ValueError", "message": str(error)}
        )
    return {"translation": TranslationService.jeringonza(input.value)}
