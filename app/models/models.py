from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    subscription_id = db.Column(db.Integer, db.ForeignKey('subscriptions.id'))

    # Method to set password
    def set_password(self, password):
        self.password = generate_password_hash(password, method='sha256')

    # Method to check password
    def check_password(self, password):
        return check_password_hash(self.password, password)

class Subscription(db.Model):
    __tablename__ = 'subscriptions'

    id = db.Column(db.Integer, primary_key=True)
    plan_name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    user = db.relationship('User', backref='subscription', lazy=True)
