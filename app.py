from flask import Flask, render_template, request
import re

app = Flask(__name__)

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email)

@app.route('/', methods=['GET', 'POST'])
def email_slicer():
    result = ""
    error = ""
    if request.method == 'POST':
        email = request.form.get('email')
        
        if not email:
            error = "Please enter an email address."
        elif not is_valid_email(email):
            error = "Invalid email format. Please enter a valid email."
        else:
            username, domain = email.split('@')
            result = f"Username: {username}, Domain: {domain}"
    
    return render_template('index.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True)
