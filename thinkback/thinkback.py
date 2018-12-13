from flask import Flask, render_template, request, session, g, redirect, url_for, abort, \
    render_template, flash
import os
from .views import about, assignments
import sqlite3

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.secret_key = b'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)

@app.route('/index')
@app.route('/')
def index():
    return render_template('/index.html')


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)


app.config.from_object(__name__)  # load config from this file , flaskr.py
# Load default config and override config from an environment variable

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'flaskr.db'),
    SECRET_KEY='super secret key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)


def connect_db():
    print("""Connects to the specific database.""")
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    print("""Opens a new database connection if there is none yet for the
	current application context.
	""")
    if not hasattr(g, 'flaskr.db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


@app.teardown_appcontext
def close_db(error):
    print("""Closes the database again at the end of the request.""")
    if hasattr(g, 'flaskr.db'):
        g.sqlite_db.close()

@app.cli.command('initdb')
def initdb_command():
    print("""Initializes the database.""")
    init_db()
    print('Initialized the database.')

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('dropdb')
def drop_db_command():
    print("Dropping database.")
    drop_db()
    print("Dropped database.")

def drop_db():
    db = get_db()
    with app.open_resource('drop.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
