# AI_Email_Assistant

A full-stack web application that uses Google Gemini AI to help you write, rewrite, and polish professional emails — generate from scratch, fix grammar, change tone, compose from a prompt, and keep a history of everything you create.


## Features

| Feature | Description |
|---|---|
| **User Authentication** | Secure signup/login with JWT-based sessions and bcrypt password hashing |
| **Generate Emails** | Create a professional email from email type, recipient, tone, and purpose |
| **Rewrite Emails** | Rewrite an existing email based on a custom instruction |
| **Grammar Checker** | Fix grammar and phrasing issues in any text |
| **Tone Changer** | Convert an email into a different tone (formal, friendly, assertive, etc.) |
| **Compose from Prompt** | Generate a full email from a single free-text prompt |
| **Email History** | Every AI-generated result is saved per user and retrievable later |


## Technologies Used

### Backend
- Python
- FastAPI
- SQLAlchemy ORM + MySQL
- JWT Authentication + bcrypt password hashing
- Google Gemini API for AI generation

### Frontend
- HTML
- CSS
- JavaScript

### Testing
- Pytest
- Pytest-Cov

### Deployment
- Docker 



## System Architecture

```text
                         ┌─────────────────────┐
                         │        USER         │
                         └──────────┬──────────┘
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FRONTEND       │
                         │    HTML/CSS/JS      │
                         └──────────┬──────────┘
                                    │
                             HTTP / REST
                                    │
                                    ▼
                         ┌─────────────────────┐
                         │      FastAPI        │
                         │      REST API       │
                         └──────────┬──────────┘
                                    │
                   ┌────────────────┼────────────────┐
                   │                │                │
                   ▼                ▼                ▼
             ┌───────────┐   ┌────────────┐   ┌─────────────┐
             │    JWT    │   │  Services  │   │ Gemini API  │
             │   Auth    │   │   Layer    │   │     AI      │
             └───────────┘   └─────┬──────┘   └─────────────┘
                                   │
                                   ▼
                            ┌─────────────┐
                            │ SQLAlchemy  │
                            └──────┬──────┘
                                   │
                                   ▼
                            ┌─────────────┐
                            │    MySQL    │
                            └─────────────┘
```


## Project Structure

```text
AI_Email_Assistant/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── auth/
│   │   │   ├── email/
│   │   │   ├── grammar/
│   │   │   ├── rewrite/
│   │   │   ├── tone/
│   │   │   ├── compose/
│   │   │   └── history/
│   │   │
│   │   ├── database/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   └── main.py
│   │
│   ├── tests/
│   ├── .env.example
│   ├── Dockerfile
│   └── requirements.txt
│
├── frontend/
│   ├── css/
│   ├── js/
│   ├── index.html
│   ├── login.html
│   ├── signup.html
│   ├── email.html
│   ├── rewrite.html
│   ├── grammar.html
│   ├── tone.html
│   ├── compose.html
│   ├── history.html
│   └── Dockerfile
│
├── docs/
│   ├── API_Documentation.md
│   ├── Database_Documentation.md
│   └── 6. Project_Architecture.md
│
├── docker-compose.yml
└── README.md
```


## Project Workflow

```text
┌──────────────────────┐
│        USER          │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      FRONTEND        │
│    HTML / CSS / JS   │
└──────────┬───────────┘
           │
           │ Login / Signup
           ▼
┌──────────────────────┐
│   FASTAPI AUTH API   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│      JWT TOKEN       │
└──────────┬───────────┘
           │
           │ Authenticated Request
           ▼
┌──────────────────────┐
│    FASTAPI ROUTE     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│  REQUEST VALIDATION   │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    SERVICE LAYER     │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│   PROMPT GENERATION  │
└──────────┬───────────┘
           │
           ▼
┌──────────────────────┐
│    GEMINI AI API     │
└──────────┬───────────┘
           │
           │ AI Response
           ▼
┌──────────────────────┐
│    SERVICE LAYER     │
└──────────┬───────────┘
           │
           ├─────────────────────┐
           │                     │
           ▼                     ▼
┌──────────────────────┐  ┌─────────────────────┐
│       MYSQL          │  │      FASTAPI        │
│   Email History      │  │    JSON Response    │
└──────────────────────┘  └──────────┬──────────┘
                                     │
                                     ▼
                           ┌─────────────────────┐
                           │      FRONTEND       │
                           │  Display AI Result  │
                           └──────────┬──────────┘
                                      │
                                      ▼
                           ┌─────────────────────┐
                           │        USER         │
                           └─────────────────────┘
```

## Installation

### Prerequisites
- Python 3.10+
- MySQL server
- A [Google Gemini API key](https://ai.google.dev/)

### 1. Clone the repository

```bash
git clone https://github.com/aditya6690/AI_Email_Assistant.git
cd AI_Email_Assistant/backend
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Copy the example file and fill in your own values:

```bash
cp .env.example .env
```

```env
# Database
DB_USER=your_mysql_user
DB_PASSWORD=your_mysql_password
DB_HOST=localhost
DB_PORT=3306
DB_NAME=ai_email_assistant

# Auth
SECRET_KEY=your_random_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60

# Gemini AI
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.0-flash
```

### 4. Run the server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

### 5. Open the frontend

Serve the `frontend/` folder with any static server (e.g. VS Code Live Server) and open `index.html`.


## API Documentation

Once the server is running, interactive Swagger docs are available at:

```
http://127.0.0.1:8000/docs
```

### Key Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| POST | `/auth/signup` | Register user |
| POST | `/auth/login` | Authenticate user |
| GET | `/auth/me` | Get current user |
| POST | `/email/generate` | Generate email |
| POST | `/rewrite/` | Rewrite email |
| POST | `/grammar/` | Check grammar |
| POST | `/tone/` | Change tone |
| POST | `/compose/` | Compose from prompt |
| GET | `/history/` | Get email history |

For full request/response schemas, see [`docs/API_Documentation.md`](docs/API_Documentation.md).


## Testing

Run the full test suite:

```bash
python -m pytest
```

Run with coverage:

```bash
python -m pytest --cov=app --cov-report=term-missing
```

**Current Coverage:** 91%
**Tests Passed:** 15


## Deployment

The app is containerized and deployable via Docker Compose (Nginx reverse proxy + FastAPI + MySQL):

```bash
docker-compose up --build
```

See [`docs/6. Project_Architecture.md`](docs/6.%20Project_Architecture.md) for the full deployment architecture.

## Future Improvements

- Email Templates
- Attachments
- User Profiles
- Admin Dashboard
- Export History
