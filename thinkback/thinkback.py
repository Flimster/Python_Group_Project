import os
from .database import database
from flask import Flask, render_template, g
from .views import about, assignments, upload, problem_upload

UPLOAD_FOLDER = './uploads'
SOLUTIONS_FOLDER = './impl'

app = Flask(__name__)

app.secret_key = b'ea983fa73ad64b649c11c15b437787a9'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SOLUTIONS_FOLDER'] = SOLUTIONS_FOLDER

# Registers the blueprints
app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)
app.register_blueprint(upload.upload_blueprint)
app.register_blueprint(problem_upload.problem_upload_blueprint)

app.config.from_object(__name__)

app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'thinkback.db'),
    SECRET_KEY='super secret key',
    USERNAME='admin',
    PASSWORD='default'
))
app.config.from_envvar('THINKBACK_SETTINGS', silent=True)


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
    if hasattr(g, 'thinkback.db'):
        g.sqlite_db.close()


@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')


@app.route('/index')
@app.route('/')
def index():
    assignment_list = database.get_assignments_with_problems()
    return render_template('assignments.html', assignment_list=assignments.filter_assignments(assignment_list, 1), flag=True)


if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)
