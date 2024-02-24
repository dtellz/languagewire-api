translations = {
    "spanish": "Hola. ¿Cómo estás?",
    "german": "Hallo. Wie geht es dir?",
    "french": "Bonjour. Comment ça va?",
    "italian": "Ciao. Come stai?",
    "danish": "Hej. Hvordan har du det?"
}

class TranslationService:
    @staticmethod
    def translate(lang: str):
        return translations[lang]
