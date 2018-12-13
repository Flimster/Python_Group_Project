from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
from .views import about, assignments, database
import sqlite3

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.secret_key = b'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)
app.register_blueprint(database.database_blueprint)

app.config.from_object(__name__)  # load config from this file , flaskr.py
# Load default config and override config from an environment variable

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='super secret key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

# Database command line tools
@app.cli.command('dropdb')
def drop_db_command():
    print("Dropping database.")
    database.drop_db()
    print("Dropped database.")


@app.cli.command('initdb')
def initdb_command():
    print("""Initializes the database.""")
    database.init_db()
    print('Initialized the database.')


@app.teardown_appcontext
def close_db(error):
    print("""Closes the database again at the end of the request.""")
    if hasattr(g, 'flaskr.db'):
        g.sqlite_db.close()


@app.route('/index')
@app.route('/')
def index():
    return render_template('/index.html')


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
