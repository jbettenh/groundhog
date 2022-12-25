from groundhog import create_app, db
from groundhog.models import Users, Sightings, Zoos

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Users": Users, "Sightings": Sightings, "Zoos": Zoos}


if __name__ == "__main__":
    app.run(host="0.0.0.0")
