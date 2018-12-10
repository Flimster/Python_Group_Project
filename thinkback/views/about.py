# thinkback/views/about.py

from flask import Blueprint

about_blueprint = Blueprint('about', __name__)

@about_blueprint.route('/about')
def about_us():
	return "A company is here"