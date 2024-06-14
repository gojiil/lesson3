from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db.init_app(app)

@app.cli.command("init-db")
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('register.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    
    password_hash = generate_password_hash(password)

    new_user = User(username=username, email=email, password_hash=password_hash)
    db.session.add(new_user)
    db.session.commit()

    # Перенаправление на другую страницу можно сделать, например, на страницу входа
    return redirect(url_for('index'))