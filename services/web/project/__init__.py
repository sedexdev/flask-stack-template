from flask import Flask

from project.connectors import db, limiter, login_manager
from project.core.views import core_blueprint


# app config
app = Flask(__name__)
app.config.from_object("project.config.Config")

# blueprints
app.register_blueprint(core_blueprint)

# connectors
db.init_app(app)
limiter.init_app(app)
login_manager.init_app(app)


# additional security headers
@app.after_request
def set_security_headers(response):
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline';"
    response.headers['X-XSS-Protection'] = "1; mode=block"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    return response
