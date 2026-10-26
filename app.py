import html
import re
from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

def sanitize_input(text):
    cleaned = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', text)
    return html.escape(cleaned)

def generate_summary(text):
    cleaned = text.strip()
    if not cleaned:
        return ""
    words = cleaned.split()
    return " ".join(words[:20])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    raw_note = request.form.get('note', '')
    
    if not raw_note or not raw_note.strip():
        abort(400, "Note cannot be empty.")
    if len(raw_note) > 5000:
        abort(400, "Note exceeds 5,000 character limit.")

    sanitized_note = sanitize_input(raw_note)
    summary = generate_summary(raw_note)

    # Save format: Summary header on top, original note directly below (NO Note: prefix)
    with open('notes.txt', 'a', encoding='utf-8') as f:
        f.write(f"Summary: {summary}\n{sanitized_note}\n---\n")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)