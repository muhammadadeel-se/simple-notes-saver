# Application Handover & Deployment Documentation

## 1. Project Overview & Live URL
- **Application Name:** Simple Notes Saver
- **Live Deployment URL:** [Railway Live URL Placehere]
- **Repository:** https://github.com/muhammadadeel-se/simple-notes-saver.git

## 2. Architecture & Summary Logic
- **Framework:** Python Flask served via Gunicorn WSGI in production.
- **Input Sanitization:** Regex cleaning strips null bytes and escape HTML controls to prevent file corruption.
- **Validation:** Enforces 400 Bad Request error status for empty notes or inputs exceeding 5,000 characters.
- **20-Word Summary Extraction:** Extracts strictly the first 20 words (`words[:20]`) and prepends `Summary: <text>` at the top of each entry in `notes.txt`.

## 3. How to Run Locally vs Production

### Local Development
1. Activate virtual environment: `venv\Scripts\activate`
2. Install dependencies: `pip install -r requirements.txt`
3. Launch development server: `python app.py` (accessible at `http://127.0.0.1:5000`)
4. Run unit test suite: `python -m unittest test_summary.py`

### Production Setup
- Served via **Gunicorn** (`gunicorn app:app`) hosted on Railway containerized infrastructure.

## 4. Operational Considerations: Ephemeral Storage
- **Current Storage Mechanism:** Notes are appended to a local text file (`notes.txt`).
- **Cloud Limitation (Ephemeral Storage):** Modern cloud platforms like Railway utilize containerized, stateless file systems. While `notes.txt` functions normally during an active container session, data on local disk is reset whenever the cloud instance restarts, redeploys, or goes to sleep.
- **Production Recommendation:** For persistent storage across server deployments, migrate local text append operations to a managed database (e.g., PostgreSQL or MongoDB) or cloud storage bucket.