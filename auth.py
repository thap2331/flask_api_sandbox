from flask import Blueprint, jsonify, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from server.models import Users
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@auth.route('/register')
def register():
    return render_template('register.html')

@auth.route("/register", methods=["POST"])
def register_post():
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    user_name = request.form.get("name")
    password_hash = generate_password_hash(user_password, method='sha256')

    existing_user = Users.query.filter_by(email=user_email).first()
    if existing_user:
        flash('Email already exists.')
        return redirect(url_for('auth.register'))

    new_user = Users(email=user_email, name=user_name, password_hash=password_hash, admin=False)

    db.session.add(new_user)
    db.session.commit()
    flash('Register successful. You can login now.')
    return redirect(url_for('auth.login'))

@auth.route("/login", methods=["GET"])
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    user_email = request.form.get("email")
    user_password = request.form.get("password")
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=user_email).first()

    if not user or not check_password_hash(user.password_hash, user_password):
        flash('Please check in your login details and try again.')
        return redirect(url_for('auth.login'))
    
    login_user(user, remember=remember) 
    return redirect(url_for('main.profile'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
