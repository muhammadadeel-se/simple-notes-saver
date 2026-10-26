# Simple Notes Saver

A Flask web application that securely ingests technician notes. The notes are safely appended to a local `notes.txt` file.

## How to run locally
1. Clone this repository.
2. Open your terminal in the project directory.
3. Create and activate a virtual environment: 
   `python -m venv venv`
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Run the application: `python app.py`
6. Open a browser and navigate to `http://127.0.0.1:5000`

## Error Handling
If a note is empty or exceeds the 5,000-character limit, a **400 Bad Request** error is returned.