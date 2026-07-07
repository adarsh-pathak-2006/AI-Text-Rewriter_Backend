# AI Text Rewriter - Backend

This is the Django backend for the AI Text Rewriter application. It exposes a RESTful API that utilizes Google's Gemini AI to rewrite user-provided text in various tones (Professional, Casual, Respectful).

## Features
- **Django REST Framework**: Structured, scalable REST API.
- **Gemini AI Integration**: Uses `google-genai` for intelligent text rewriting.
- **Production Ready**: Configured with `dj-database-url`, `gunicorn`, and `whitenoise` for easy deployment on Render.
- **CORS Enabled**: Ready to connect seamlessly with the Next.js frontend.

## Local Development

### 1. Requirements
- Python 3.10+
- `pip` package manager

### 2. Setup
Clone the repository, create a virtual environment, and install dependencies:
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# macOS/Linux: source venv/bin/activate

pip install -r requirements.txt
```

### 3. Environment Variables
Copy the `.env.example` file to create your own `.env` file:
```bash
cp .env.example .env
```
Ensure you provide your Google Gemini API key:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 4. Database Migrations
Run the initial migrations to set up your local SQLite database:
```bash
python manage.py migrate
```

### 5. Run the Server
```bash
python manage.py runserver
```
The API will be available at `http://127.0.0.1:8000/api/all/`.

## Deployment to Render
This backend is configured for easy deployment on [Render](https://render.com/).

1. Create a new **Web Service** on Render and connect this repository.
2. Under settings, use the following:
   - **Build Command**: `./build.sh`
   - **Start Command**: `gunicorn ai_text_rewriter.wsgi:application`
3. Add the following Environment Variables in the Render dashboard:
   - `DEBUG`: `False`
   - `ALLOWED_HOSTS`: `your-app-name.onrender.com`
   - `GEMINI_API_KEY`: `your_gemini_api_key_here`
   - `DATABASE_URL`: *(Render will provide this automatically if you attach a PostgreSQL database)*

The `build.sh` script handles dependency installation, static file collection, and database migrations.
