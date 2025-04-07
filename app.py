from flask import Flask, request, jsonify, send_file, render_template, redirect, url_for, session
import os
from AIMemeGenerator import generate
import io
from functools import wraps
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this to a secure secret key

# Simulated user database (replace with a real database in production)
users = {
    'test@example.com': {
        'password': 'password123',
        'name': 'Test User'
    }
}

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

def is_valid_email(email):
    # Basic email validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def is_valid_password(password):
    # Password must be at least 8 characters
    return len(password) >= 8

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    
    data = request.json
    name = data.get('name', '').strip()
    email = data.get('email', '').strip().lower()
    password = data.get('password', '')

    # Validation
    if not name or not email or not password:
        return jsonify({'error': 'All fields are required'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Invalid email format'}), 400

    if not is_valid_password(password):
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    if email in users:
        return jsonify({'error': 'Email already registered'}), 400

    # Store new user
    users[email] = {
        'password': password,
        'name': name
    }

    return jsonify({'success': True, 'message': 'Registration successful'})

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    
    data = request.json
    email = data.get('email', '').strip().lower()
    password = data.get('password')
    
    if email in users and users[email]['password'] == password:
        session['user'] = email
        return jsonify({'success': True})
    
    return jsonify({'error': 'Invalid email or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user', None)
    return jsonify({'success': True})

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')

@app.route('/api/user')
@login_required
def get_user():
    user_email = session['user']
    return jsonify({
        'email': user_email,
        'name': users[user_email]['name']
    })

@app.route('/generate', methods=['POST'])
@login_required
def generate_meme():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        
        # Generate the meme using the existing function
        result = generate(
            user_entered_prompt=prompt,
            noUserInput=True,  # Don't prompt for user input
            noFileSave=True    # Don't save to file system
        )
        
        # Get the virtual meme file from the result
        if result and isinstance(result, list) and len(result) > 0:
            meme_info = result[0]  # Get first meme result
            virtual_meme_file = meme_info.get('virtual_meme_file')
            
            if virtual_meme_file:
                # Seek to beginning of file
                virtual_meme_file.seek(0)
                
                # Return the image directly
                return send_file(
                    virtual_meme_file,
                    mimetype='image/png'
                )
        
        return jsonify({'error': 'Failed to generate meme'}), 500
        
    except Exception as e:
        print(f"Error generating meme: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 