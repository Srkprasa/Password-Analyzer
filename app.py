from flask import Flask, render_template, request
import re

app = Flask(__name__, template_folder='../templates')

def analyze_password_strength(password):
    length = len(password)
    has_lower = re.search(r'[a-z]', password) is not None
    has_upper = re.search(r'[A-Z]', password) is not None
    has_digit = re.search(r'\d', password) is not None
    has_special = re.search(r'[^A-Za-z0-9]', password) is not None

    score = 0
    if length >= 8:
        score += 1
    if has_lower:
        score += 1
    if has_upper:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

    if score <= 2:
        return "Weak password"
    elif score == 3 or score == 4:
        return "Medium strength password"
    else:
        return "Strong password"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    if request.method == 'POST':
        password = request.form['password']
        result = analyze_password_strength(password)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
