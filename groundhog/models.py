from datetime import datetime
from groundhog import db


class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(
        db.String(100), index=True, nullable=False, unique=True
    )
    hash = db.Column(db.String(1000), nullable=False)
    email = db.Column(db.String(100), index=True, nullable=False, unique=True)
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

    def __repr__(self):
        return f'<Sighting "{self.name}">'


class Zoos(db.Model):
    __tablename__ = "zoos"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(200))
    description = db.Column(db.String(1000))
    has_groundhog = db.Column(
        db.Boolean(create_constraint=True, name="has_groundhog")
    )

    def __init__(self, name, website, description, has_groundhog):
        self.name = name
        self.website = website
        self.description = description
        self.has_groundhog = has_groundhog

    def __repr__(self):
        return f'<Zoo "{self.name}">'
