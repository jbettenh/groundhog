import os
from flask import Flask, render_template
from flask_session import Session


def create_app(test_config=None):
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

    # Register blueprints
    from groundhog import auth

    app.register_blueprint(auth.bp)

    @app.route("/", methods=["GET"])
    def index():
        """Show homepage"""
        return render_template("index.html")

    return app
