import csv
import os
import re
import datetime
import jwt
import hashlib
from flask import Blueprint, request, jsonify
import jwt

user_routes = Blueprint('user_routes', __name__)
SECRET_KEY = os.environ.get('SECRET_KEY')

DATA_DIR = os.path.join(os.getcwd(), 'data')
USERS_FILE = os.path.join(DATA_DIR, 'users.csv')
os.makedirs(DATA_DIR, exist_ok=True)

if not os.path.exists(USERS_FILE):
    with open(USERS_FILE, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['username', 'email', 'password'])

@user_routes.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Missing required fields. Try again with correct fields!'}), 400

    if len(password) < 8:
        return jsonify({'error': 'Password must be at least 8 characters long'}), 400

    if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", email):
        return jsonify({'error': 'Invalid email address'}), 400

    if not re.search(r"[A-Z]", password):
        return jsonify({'error': 'Password must contain at least one uppercase letter'}), 400

    if not re.search(r"[a-z]", password):
        return jsonify({'error': 'Password must contain at least one lowercase letter'}), 400

    if not re.search(r"\d", password):
        return jsonify({'error': 'Password must contain at least one digit'}), 400

    if not re.search(r"[ !@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password):
        return jsonify({'error': 'Password must contain at least one special character'}), 400

    with open(USERS_FILE, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[1] == email:
                return jsonify({'error': 'User with this email already exists'}), 400

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    with open(USERS_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([username, email, hashed_password])

    token = jwt.encode({
        'username': username,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30)
    }, SECRET_KEY, algorithm='HS256')
    return jsonify({'message': 'User registered successfully', 'token': token}), 201

