# Covra Chat

<div align="center">
  <img src="frontend/src/assets/covra-icon.png" alt="Covra Logo" width="100"/>
  <h1>Your Cover Letter Generator</h1>
</div>

A modern web application that generates personalized cover letters using AI. Built with React, FastAPI, and powered by Cohere AI.

## Features

- Generate professional cover letters based on your CV and job descriptions
- Clean and intuitive user interface
- Powered by Cohere AI's advanced language model
- Real-time generation with loading indicators
- Responsive design

## Prerequisites

- Python 3.8 or higher
- Node.js 16 or higher
- A Cohere AI API key
- Docker & Docker Compose
- (Optional) Kubernetes & kubectl + minikube or a cloud provider

## Setup

### Backend Setup

1. Navigate to the backend directory:
```bash
cd backend
```

2. Create and activate a virtual environment:
```bash
# Windows
python -m venv venv
.
env\Scripts ctivate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the backend directory and add your Cohere API key:
```
COHERE_API_KEY=your_api_key_here
```

5. Run Alembic migrations (ensure database is running):
```bash
alembic upgrade head
```

6. Start the backend server:
```bash
uvicorn main:app --reload
```

The backend will be running at `http://localhost:8000`

### Frontend Setup

1. Open a new terminal and navigate to the frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

The frontend will be running at `http://localhost:5173`

## Docker Setup

1. Ensure you have Docker and Docker Compose installed.
2. Build and start the containers:
```bash
docker-compose up --build
```
3. Access the frontend at `http://localhost:5173` and the backend at `http://localhost:8000`.

> Note: Modify environment variables in `.env` and `docker-compose.yml` as needed.

## Kubernetes Setup (Optional)

1. Make sure `kubectl` and `minikube` are installed and configured.
2. Start minikube:
```bash
minikube start
```
3. Apply the Kubernetes manifests:
```bash
kubectl apply -f k8s/
```
4. To access the services:
```bash
minikube service covra-frontend
minikube service covra-backend
```

> Make sure your Kubernetes manifests include ConfigMaps or Secrets with the required environment variables.

## How to Use

1. Open your browser and go to `http://localhost:5173`
2. You'll see a clean interface with a text input area
3. First, paste your CV into the input field and click "Send"
4. Then, paste the job description you're applying for and click "Send"
5. The AI will generate a personalized cover letter based on your CV and the job description
6. The generated cover letter will appear in the chat interface

## Technologies Used

- **Frontend:**
  - React
  - TypeScript
  - Tailwind CSS
  - Vite

- **Backend:**
  - FastAPI
  - Python
  - LangChain
  - Cohere AI
  - **Alembic** (for database migrations)
  - **Docker** (for containerization)
  - **Kubernetes** (for orchestration and deployment)

## Note

Make sure both the backend and frontend servers are running simultaneously for the application to work properly. The backend handles the AI processing while the frontend provides the user interface.