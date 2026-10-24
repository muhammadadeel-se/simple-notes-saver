from flask import Flask, render_template, request
import re
import html

app = Flask(__name__)

def sanitize_input(text):
    cleaned_text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f\x7f-\x9f]', '', text)
    return html.escape(cleaned_text)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save():
    # Mentor ne textarea ka naam 'note' rakhne ko kaha hai
    user_input = request.form.get('note', '').strip()
    
    # Check 1: Empty Input
    if not user_input:
        return 'Error: Note cannot be empty. <a href="/">Return to form</a>', 400
        
    # Check 2: Length Limit
    if len(user_input) > 5000:
        return 'Error: Note exceeds the 5000 character limit. <a href="/">Return to form</a>', 400

    # Check 3 & 4: Control Characters & HTML Escaping
    sanitized_data = sanitize_input(user_input)
    
    if sanitized_data:
        # File ko 'a' (append) mode mein open kar rahe hain
        with open('notes.txt', 'a', encoding='utf-8') as f:
            f.write(sanitized_data + '\n---\n')
            
    return 'Notes saved successfully. <a href="/">Return to form</a>'

if __name__ == '__main__':
    app.run(debug=True)