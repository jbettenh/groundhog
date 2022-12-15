from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()
migrate = Migrate()
sess = Session()


def create_app(config_class=Config):
    # Create the Flask application
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)

    # Register blueprints
    from groundhog import auth, routes

    app.register_blueprint(auth.bp)
    app.register_blueprint(routes.bp)

    return app


from groundhog import models
