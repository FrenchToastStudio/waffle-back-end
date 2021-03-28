from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, make_response, jsonify
)

blueprint = Blueprint('blueprint', __name__)

@blueprint.route('/')
def hello_world():
    return 'Hello, World!'
