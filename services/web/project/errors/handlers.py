from flask import Blueprint, render_template
from typing import Tuple

error_blueprint = Blueprint(
    'error',
    __name__,
    template_folder='templates'
)


@error_blueprint.app_errorhandler(401)
def error_401(error) -> Tuple:
    return render_template('401.html', error=error), 401


@error_blueprint.app_errorhandler(404)
def error_404(error) -> Tuple:
    return render_template('404.html', error=error), 404


@error_blueprint.app_errorhandler(500)
def error_500(error) -> Tuple:
    return render_template('500.html', error=error), 500