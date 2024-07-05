import os

basedir = os.path.dirname(os.path.dirname(__file__))


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")
    SQLALCHEMY_TACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
