
from email import message
import random
from flask import Blueprint, flash, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

views = Blueprint('views', __name__)


@views.route('/')
@login_required
def home():
    return render_template('home.html', user=current_user)

@views.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        oldpass = request.form.get('oldpass')
        newpass = request.form.get('newpass')
        confirmnewpass = request.form.get('confirmnewpass')
        if check_password_hash(current_user.password, oldpass):
            if newpass == confirmnewpass:
                current_user.password = generate_password_hash(newpass, method='sha256')
                db.session.commit()
                flash('Password updated', category='success')
            else:
                flash("New passwords don't match", category='error')
        else:
            flash("Incorrect password, try again", category='error')
    return render_template('profile.html', user=current_user)

messages = []


