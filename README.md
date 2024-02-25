# LanguageWire API

The LanguageWire API is a simple REST API designed to demonstrate translations into five languages (Spanish, German, French, Italian, Danish) and a fun transformation into Jeringonza. It's built with FastAPI and Python 3.12.2, showcasing REST API development best practices.

## Table of Contents

- [Installation](#installation)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
- [Running the API](#running-the-api)
- [Usage](#usage)
- [Architecture](#architecture)
- [Packaging and running with Docker](#packaging-and-running-with-docker)

## Installation

### Prerequisites

Python 3.12.2 or later

### Setup

Clone the repository and navigate to the project directory to set up a virtual environment:

```bash
git clone https://github.com/yourusername/languagewire-api.git
cd languagewire-api

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Start the API with Uvicorn on the local development server:

```bash
uvicorn server.main:app --reload
```

The API will be available at [http://localhost:8000](http://localhost:8000)

## Usage

The API provides two main endpoints:

```/translations/translate```

Accepted Parameters:

* text: Fixed phrase "Hello. How are you?"

* lang: Target supported language (spanish, german, french, italian, danish)

Example Request:

```bash
curl -X 'GET' \
  'http://localhost:8000/translations/translate?text=Hello.%20How%20are%20you%3F&lang=french' \
  -H 'accept: application/json'
```

```/translations/jeringonza```

Transforms any given text into Jeringonza, a playful language game.

Accepted Parameters:

* text: Any text to be transformed into Jeringonza

Example Request:

```bash
curl -X 'GET' \
  'http://localhost:8000/translations/jeringoza?text=biblioteca' \
  -H 'accept: application/json'
```

## Architecture

The API is structured around FastAPI for handling HTTP requests, with a clear separation between the routing layer (routers), data models (models), and business logic (services). This modular architecture ensures ease of maintenance and scalability.

## Packaging and running with Docker

```bash
docker build -t languagewire-api .
docker run -d --name languagewire-api-instance -p 8000:8000 languagewire-api
```
