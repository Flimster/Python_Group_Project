# thinkback/views/profile.py

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound

simple_page = Blueprint('simple_page', __name__,
                        template_folder='template')
@simple_page.route('/', defaults={'page': 'index'})
@simple_page.route('/<page>')
def show(page):
    print('Hello World')
    try:
        return render_template('pages/{}.html'.format(page))
    except TemplateNotFound:
        abort(404)