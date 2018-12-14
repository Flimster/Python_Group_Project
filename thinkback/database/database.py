# thinkback/database.py

import sqlite3
from flask import g
from flask import current_app as app
from ..models import Problem, Assignment


def drop_db():
    db = get_db()
    with app.open_resource('drop.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
        current application context.
        """
    if not hasattr(g, 'thinkback.db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db_assignments():
	assignment_list = []
	db = get_db()
	cur = db.execute('select * from assignments')
	entries = cur.fetchall()
	for assignment in entries:
		assignment_list.append(Assignment(
			assignment['a_id'], assignment['a_name'], assignment['a_active']))
	return assignment_list


def get_db_problems():
	problem_list = []
	db = get_db()
	cur = db.execute('select * from problems')
	entries = cur.fetchall()
	for problem in entries:
		problem_list.append(Problem(
			problem['p_id'], problem['a_id'], problem['p_name'], problem['p_desc'], problem['p_solution_name']))
	return problem_list


def get_single_problem(problem_id):
	db = get_db()
	cur = db.execute(
		'select * from problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	problem = Problem(entry['p_id'], entry['a_id'], entry['p_name'],
					  entry['p_desc'], entry['p_solution_name'])
	return problem