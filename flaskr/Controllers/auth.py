from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify
)

auth_blueprint = Blueprint('auth_blueprint', __name__)

@auth_blueprint.route('/connexion')
def hello_world():
    return 'This will be a login'
