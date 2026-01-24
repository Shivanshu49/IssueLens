# 🔍 IssueLens

**AI-powered real-time bug fix explainer for GitHub repositories**

[![FastAPI](https://img.shields.io/badge/FastAPI-0.109+-green.svg)](https://fastapi.tiangolo.com)
[![React](https://img.shields.io/badge/React-18+-blue.svg)](https://reactjs.org)
[![Python](https://img.shields.io/badge/Python-3.11+-yellow.svg)](https://python.org)

---

## 📋 Problem Statement

Developers spend **~30% of their time** understanding existing code and bug fixes. When reviewing commits or investigating production issues, key questions often go unanswered:

- *"What exactly did this commit fix?"*
- *"Why was this change necessary?"*
- *"Could this fix introduce regressions?"*

Code review comments are sparse. Commit messages are cryptic. Knowledge gets lost.

---

## 💡 Solution

**IssueLens** monitors GitHub repositories in real-time and automatically generates AI-powered explanations for bug fixes. It bridges the gap between code changes and human understanding.

### Key Features

- 🔄 **Real-time GitHub Webhooks** — Instant capture of push events, issues, and PRs
- 🤖 **AI Explanations** — Natural language summaries of what changed and why
- 📊 **Live Dashboard** — Track bug fixes, open issues, and potential regressions
- 📡 **Activity Feed** — Stream of recent repository events
- ⚡ **Pathway Integration** — Real-time data pipeline for scalable event processing

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                              GitHub                                      │
│                                │                                         │
│                         Webhook Events                                   │
│                     (push, issues, PRs)                                  │
│                                │                                         │
│                                ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                     FastAPI Backend                               │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │   │
│  │  │  Webhooks   │  │  Dashboard  │  │     AI Explain          │   │   │
│  │  │  /webhooks  │  │  /dashboard │  │     /explain            │   │   │
│  │  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘   │   │
│  │         │                │                      │                 │   │
│  │         ▼                ▼                      ▼                 │   │
│  │  ┌─────────────────────────────────────────────────────────────┐ │   │
│  │  │                    Services Layer                           │ │   │
│  │  │  ┌───────────┐ ┌───────────┐ ┌───────────┐ ┌─────────────┐  │ │   │
│  │  │  │  GitHub   │ │   Diff    │ │  Pathway  │ │     AI      │  │ │   │
│  │  │  │  Service  │ │  Service  │ │  Service  │ │   Service   │  │ │   │
│  │  │  └───────────┘ └───────────┘ └───────────┘ └─────────────┘  │ │   │
│  │  └─────────────────────────────────────────────────────────────┘ │   │
│  └──────────────────────────────────────────────────────────────────┘   │
│                                │                                         │
│                                ▼                                         │
│  ┌──────────────────────────────────────────────────────────────────┐   │
│  │                    React Frontend                                 │   │
│  │  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐   │   │
│  │  │    Home     │  │  Dashboard  │  │       Features          │   │   │
│  │  │    Page     │  │    Page     │  │         Page            │   │   │
│  │  └─────────────┘  └─────────────┘  └─────────────────────────┘   │   │
│  └──────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Frontend** | React 18, Vite, TailwindCSS |
| **Backend** | Python 3.11, FastAPI, Pydantic |
| **Real-time** | Pathway (streaming data pipeline) |
| **AI** | OpenAI GPT-4 (pluggable) |
| **Integration** | GitHub Webhooks, REST API |
| **DevOps** | Docker, uvicorn |

---

## 🚀 Quick Start

### Prerequisites

- Python 3.11+
- Node.js 18+
- GitHub account (for webhooks)

### Backend Setup

```bash
cd Backend
python -m venv venv
.\venv\Scripts\Activate.ps1   # Windows
source venv/bin/activate       # Linux/Mac

pip install -r requirements.txt
cp .env.example .env
# Edit .env with your API keys

python -m uvicorn app.main:app --reload --port 8000
```

### Frontend Setup

```bash
cd Frontend
npm install
npm run dev
```

### Access

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000/docs
- **Health Check:** http://localhost:8000/api/v1/health

---

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/health` | GET | Health check |
| `/api/v1/webhooks/github` | POST | GitHub webhook receiver |
| `/api/v1/dashboard/summary` | GET | Bug fix statistics |
| `/api/v1/activity` | GET | Live activity feed |
| `/api/v1/explain` | POST | AI explanation for commits |
| `/api/v1/issues` | GET | List tracked issues |

---

## 🎬 Demo Flow

1. **Connect Repository** — Configure GitHub webhook to point to IssueLens
2. **Push a Bug Fix** — Commit with message like "Fix memory leak in auth module"
3. **Webhook Triggers** — IssueLens receives the push event instantly
4. **AI Analysis** — The diff is parsed and sent to AI for explanation
5. **Dashboard Updates** — Live feed shows the fix with human-readable summary
6. **Team Visibility** — Everyone understands what changed without reading code

---

## 📁 Project Structure

```
IssueLens/
├── Backend/
│   ├── app/
│   │   ├── api/routes/       # API endpoints
│   │   ├── core/             # Config, logging, security
│   │   ├── services/         # Business logic
│   │   ├── schemas/          # Pydantic models
│   │   └── utils/            # Helpers, diff parser
│   ├── pathway/              # Real-time pipeline
│   ├── tests/                # Test suite
│   └── requirements.txt
│
├── Frontend/
│   ├── src/
│   │   ├── components/       # Reusable UI components
│   │   └── pages/            # Page components
│   └── package.json
│
└── README.md
```

---

## 🔮 Future Improvements

- [ ] **Full Pathway Integration** — Stream processing for high-volume repos
- [ ] **Slack/Discord Notifications** — Alert teams on critical fixes
- [ ] **Regression Detection** — ML-based risk scoring for changes
- [ ] **PR Summaries** — Auto-generate PR descriptions
- [ ] **Multi-repo Support** — Monitor organization-wide repositories
- [ ] **Historical Analytics** — Bug trends and fix patterns over time
- [ ] **Code Context RAG** — Use codebase embeddings for better explanations

---

## 👥 Team

Built with ☕ and 💻 during the hackathon.

---

## 📄 License

MIT License - feel free to use, modify, and distribute.

---

<p align="center">
  <b>IssueLens</b> — Understanding bug fixes shouldn't require reading every line of code.
</p>
