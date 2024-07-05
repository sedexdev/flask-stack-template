from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from project.connectors import db, login_manager
from project.core.views import core_blueprint


# app config
app = Flask(__name__)
app.config.from_object("project.config.Config")

# blueprints
app.register_blueprint(core_blueprint)

# connectors
db.init_app(app)
login_manager.init_app(app)
