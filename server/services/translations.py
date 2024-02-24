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
    
    @staticmethod
    def jeringoza(text: str) -> str:
        vowels = "aeiouAEIOU"
        jeringoza_text = ""
        for letter in text:
            if letter in vowels:
                jeringoza_text += f"{letter}p{letter.lower()}"
            else:
                jeringoza_text += letter
        return jeringoza_text
