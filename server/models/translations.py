from pydantic import BaseModel, validator

class TranslationQuery(BaseModel):
    text: str
    lang: str

    @validator('lang')
    def validate_language(cls, v):
        supported_languages = ['spanish', 'german', 'french', 'italian', 'danish']
        if v.lower() not in supported_languages:
            raise ValueError('Unsupported language')
        return v.lower()

    @validator('text')
    def validate_text(cls, v):
        if v != "Hello. How are you?":
            raise ValueError('Incorrect text to translate. Introduce "Hello. How are you?"')
        return v
    