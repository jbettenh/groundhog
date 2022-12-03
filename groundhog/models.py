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
