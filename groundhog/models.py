from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    hash = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    name_first = db.Column(db.String(100))
    name_last = db.Column(db.String(100))

    def __init__(self, username, hash, email, name_first=None, name_last=None):
        self.username = username
        self.hash = hash
        self.email = email
        self.name_first = name_first
        self.name_last = name_last

    def __repr__(self):
        return f'<User "{self.username}">'


class Sightings(db.Model):
    __tablename__ = "sightings"

    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(1000))

    def __init__(self, name, latitude, longitude, description=None):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.description = description
