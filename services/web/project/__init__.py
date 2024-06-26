from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project.core.views import core_blueprint


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

app.register_blueprint(core_blueprint)
