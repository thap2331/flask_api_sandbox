from flask import Blueprint, render_template, request, flash, url_for, redirect
from flask_login import login_required, current_user
from server.models import Users
from werkzeug.security import check_password_hash
from app import db
import secrets
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    if request.method=="GET":
        user_email = request.form.get("email")
        button_name = 'Generate'
        if current_user.api_key:
            button_name = 'Regenerate'
        return render_template('profile.html', name=current_user.name, button_name=button_name,
                                token=current_user.api_key)

    elif request.method=="POST":
        user_email = request.form.get("email")
        user_password = request.form.get("password")
        user = Users.query.filter_by(email=user_email).first()

        if not user or not check_password_hash(user.password_hash, user_password):
            flash('Please check in your login details and try again.')
            return redirect(url_for('main.profile'))
        
        # token = Users().encode_auth_token(current_user.id)
        api_key = secrets.token_urlsafe(16)
        user.api_key = api_key
        user.api_key_iat = datetime.now().strftime('%Y-%m-%d')
        db.session.commit()
        button_name = 'Generate'
        if current_user.api_key:
            button_name = 'Regenerate'
        return render_template('profile.html', name=current_user.name, button_name=button_name,
                                api_key=current_user.api_key)
        