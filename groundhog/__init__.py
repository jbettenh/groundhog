import os
import click
from flask import Flask
from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from config import Config  # noqa F401

db = SQLAlchemy()
migrate = Migrate()
sess = Session()


def create_app():
    # Create the Flask application
    app = Flask(__name__, instance_relative_config=False)
    CONFIG_TYPE = os.environ.get("CONFIG_TYPE", default="config.Config")
    app.config.from_object(CONFIG_TYPE)
    app.cli.add_command(create_zoos)

    # Initialize Flask extensions here
    db.init_app(app)
    migrate.init_app(app, db)
    sess.init_app(app)

    with app.app_context():
        # Register blueprints
        from groundhog import auth, routes

        app.register_blueprint(auth.bp)
        app.register_blueprint(routes.bp)

        return app


from groundhog import models  # noqa: E402, F401


@click.command()
def create_zoos():
    """Insert default zoos."""
    db.session.add(
        models.Zoos(
            name="Berlin Zoological Garden",
            website="""https://www.zoo-berlin.de/de""",
            description="""Von A wie Ameisenbär bis Z wie
             Zweifingerfaultier – im Herzen der Großstadt Berlin
              erwartet Sie die faszinierende Welt der Tiere.""",
            has_groundhog=True,
        )
    )
    db.session.add(
        models.Zoos(
            name="Toronto Zoo",
            website="https://www.torontozoo.com/",
            description="CONNECTING PEOPLE TO WILDLIFE SINCE 1974",
            has_groundhog=True,
        )
    )
    db.session.commit()

    click.echo("Added some seed zoos to the database")
