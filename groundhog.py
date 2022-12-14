from groundhog import create_app, db
from groundhog.models import Users, Sightings

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Users": Users, "Sightings": Sightings}
