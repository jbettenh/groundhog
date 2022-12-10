import os
from flask import Flask
from flask_session import Session


def create_app():
    # Create the Flask application
    app = Flask(__name__, instance_relative_config=True)

    config = os.environ.get("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config)

    # Initialize Flask extensions here
    sess = Session()
    sess.init_app(app)

    # Initialize db
    from groundhog.models import db

    db.init_app(app)
    """
      with app.app_context():
        db.drop_all()
        db.create_all()
    
    """

    # Register blueprints
    from groundhog import auth, routes

    app.register_blueprint(auth.bp)
    app.register_blueprint(routes.bp)

    return app
