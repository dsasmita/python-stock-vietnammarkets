from flask import Blueprint, jsonify

module_home = Blueprint('module_home', __name__, template_folder='templates')


@module_home.route('/')
def index():
    data = {'page': 'leadbook', 'title': 'api'}
    return jsonify(data)