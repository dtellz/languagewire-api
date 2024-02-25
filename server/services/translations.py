class TranslationService:

    translations: dict = {
    "spanish": "Hola. ¿Cómo estás?",
    "german": "Hallo. Wie geht es dir?",
    "french": "Bonjour. Comment ça va?",
    "italian": "Ciao. Come stai?",
    "danish": "Hej. Hvordan har du det?"
    }

    @staticmethod
    def translate(lang: str) -> str:
        return TranslationService.translations[lang]
    
    @staticmethod
    def jeringonza(text: str) -> str:
        vowels = "aeiouAEIOU"
        jeringonza_text = ""
        for letter in text:
            if letter in vowels:
                jeringonza_text += f"{letter}p{letter.lower()}"
            else:
                jeringonza_text += letter
        return jeringonza_text
