from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify
)

hello_blueprint = Blueprint('hello_blueprint0', __name__)

@hello_blueprint.route('/')
def hello_world():
    return 'Hello, World!'
