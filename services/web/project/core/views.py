from flask import Blueprint, jsonify


core_blueprint = Blueprint(
    'core',
    __name__,
    template_folder='templates'
)


@core_blueprint.route("/")
def hello_world():
    return jsonify(hello="world")
