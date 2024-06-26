import os

basedir = os.path.dirname(os.path.dirname(__file__))


class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TACK_MODIFICATIONS = False
