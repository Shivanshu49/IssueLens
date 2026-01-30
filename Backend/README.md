# IssueLens Backend

Real-time AI platform that monitors GitHub repositories and explains bug fixes.

## Tech Stack

- **Python 3.11+**
- **FastAPI** - Modern web framework
- **Pathway** - Real-time data processing
- **Pydantic** - Data validation
- **GitHub Webhooks** - Event monitoring

## Project Structure

```
backend/
├── app/
│   ├── main.py              # FastAPI application entry
│   ├── core/                 # Configuration & utilities
│   ├── api/                  # API routes
│   ├── services/             # Business logic
│   ├── models/               # Database models
│   ├── schemas/              # Pydantic schemas
│   ├── db/                   # Database configuration
│   └── utils/                # Helper functions
├── pathway/                  # Real-time pipeline
├── tests/                    # Test suite
├── .env.example             # Environment template
├── Dockerfile               # Container config
└── requirements.txt         # Dependencies
```

## Quick Start

### 1. Setup Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
.\venv\Scripts\activate   # Windows

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure Environment

```bash
# Copy environment template
cp .env.example .env

# Edit .env with your credentials
# - GITHUB_TOKEN
# - GITHUB_WEBHOOK_SECRET
# - OPENAI_API_KEY (optional)
```

### 3. Run the Server

```bash
# Development mode
uvicorn app.main:app --reload

# Production mode
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

### 4. Access API

- **API Docs**: http://localhost:8000/api/v1/docs
- **Health Check**: http://localhost:8000/api/v1/health

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/health` | GET | Health check |
| `/api/v1/webhooks/github` | POST | GitHub webhook receiver |
| `/api/v1/issues` | GET | List tracked issues |
| `/api/v1/issues/{id}` | GET | Get issue with explanation |
| `/api/v1/dashboard/stats` | GET | Dashboard statistics |

## Running Tests

```bash
pytest tests/ -v
```

## Docker

```bash
# Build image
docker build -t issuelens-backend .

# Run container
docker run -p 8000:8000 --env-file .env issuelens-backend
```

## GitHub Webhook Setup

1. Go to your repository settings
2. Navigate to Webhooks → Add webhook
3. Set Payload URL to: `https://your-domain.com/api/v1/webhooks/github`
4. Set Content type to: `application/json`
5. Set Secret to match your `GITHUB_WEBHOOK_SECRET`
6. Select events: Push, Issues, Pull requests

## Development Notes

- The Pathway pipeline runs separately for real-time processing
- AI explanations are generated asynchronously
- Database integration is optional (SQLAlchemy ready)

### Running Pathway Pipeline
To start the real-time data processing pipeline (Linux/macOS only):

```bash
# Pathway is not supported on Windows
# Install on Linux/Mac:
# pip install pathway
# python pathway/pipeline.py
```

## License

MIT
