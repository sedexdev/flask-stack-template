from flask.cli import FlaskGroup
from werkzeug.security import generate_password_hash

from project import app, db
from project.models import User

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command("seed_db")
def seed_db():
    hashed_password = generate_password_hash("somePassword123", method='pbkdf2:sha256')
    new_user = User(
        email="admin@application.test.uk",
        username="app_admin",
        password=hashed_password
    )
    db.session.add(new_user)
    db.session.commit()


if __name__ == "__main__":
    cli()
