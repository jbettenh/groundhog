from groundhog import db
from groundhog.models import Sightings


def test_db_insert(app):

    with app.app_context():
        sighting = Sightings(
            "test", 41.878876, -87.635918, "This is a test description"
        )
        db.session.add(sighting)
        db.session.commit()

        assert db.session.query(Sightings).one()
