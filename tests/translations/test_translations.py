#from starlette.testclient import TestClient
from fastapi.testclient import TestClient
from server.main import app

client = TestClient(app)

def test_translate_success():
    for lang, expected_translation in {
        "spanish": "Hola. ¿Cómo estás?",
        "german": "Hallo. Wie geht es dir?",
        "french": "Bonjour. Comment ça va?",
        "italian": "Ciao. Come stai?",
        "danish": "Hej. Hvordan har du det?"
    }.items():
        response = client.get("/translations/translate", params={"text": "Hello. How are you?", "lang": lang})
        assert response.status_code == 200
        assert response.json() == {"translation": expected_translation}

def test_translate_unsupported_language():
    response = client.get("/translations/translate", params={"text": "Hello. How are you?", "lang": "klingon"})
    assert response.status_code == 422
    assert "Unsupported language" in response.json()["message"]

def test_translate_incorrect_text():
    response = client.get("/translations/translate", params={"text": "Goodbye", "lang": "spanish"})
    assert response.status_code == 422
    assert "Incorrect text to translate" in response.json()["mesage"]

def test_jeringonza_success():
    response = client.get("/translations/jeringonza", params={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"translation": "hepellopo"}

def test_jeringonza_failure():
    response = client.get("/translations/jeringonza", params={"text": "hello123"})
    assert response.status_code == 422
    assert "Input must be alphabetical characters only" in response.json()["message"]
