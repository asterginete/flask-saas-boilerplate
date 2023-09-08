from flask import render_template, Blueprint, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home route."""
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return render_template('main/index.html', title='Welcome to My SaaS App')

@main.route('/dashboard')
@login_required
def dashboard():
    """User dashboard route."""
    return render_template('main/dashboard.html', title='Dashboard', user=current_user)
