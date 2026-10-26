import html
import re
from flask import Flask, render_template, request, abort, redirect, url_for

app = Flask(__name__)

def sanitize_input(text):
    # Remove null bytes and clean control characters
    cleaned = re.sub(r'[\x00-\x08\x0B\x0C\x0E-\x1F]', '', text)
    return html.escape(cleaned)

def generate_summary(text):
    cleaned = text.strip()
    if not cleaned:
        return ""
    
    # Match the first sentence ending with ., !, or ?
    match = re.search(r'([^.!?]*[.!?])', cleaned)
    if match:
        first_sentence = match.group(1).strip()
        if len(first_sentence) <= 120:
            return first_sentence

    # Fallback: Truncate to 120 chars if no short sentence exists
    if len(cleaned) > 120:
        return cleaned[:120].strip() + "..."
    return cleaned

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    raw_note = request.form.get('note', '')
    
    # Validation checks
    if not raw_note or not raw_note.strip():
        abort(400, "Note cannot be empty.")
    if len(raw_note) > 5000:
        abort(400, "Note exceeds 5,000 character limit.")

    sanitized_note = sanitize_input(raw_note)
    summary = generate_summary(raw_note)

    # Append formatted entry to notes.txt
    with open('notes.txt', 'a', encoding='utf-8') as f:
        f.write(f"Summary: {summary}\nNote: {sanitized_note}\n---\n")

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)