# thinkback/database.py

import sqlite3
from flask import g
from flask import current_app as app
from ..models import Problem, Assignment

#Drops all database tables and erases all data
def drop_db():
	db = get_db()
	with app.open_resource('./database/drop.sql', mode='r') as f:
		db.cursor().executescript(f.read())
	db.commit()

#Creates the tables for the database and inserts some example data into it
def init_db():
	db = get_db()
	with app.open_resource('./database/schema.sql', mode='r') as f:
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

#Gets all assignments in the database and the problems for those assignments
def get_assignments_with_problems():
	assignment_list = get_db_assignments()
	problem_list = get_db_problems()
	for assignment in assignment_list:
		for problem in problem_list:
			if problem.assignment_id == assignment.id:
				assignment.problem_list.append(problem)
	return assignment_list

#Gets all assignments from the database
def get_db_assignments():
	assignment_list = []
	db = get_db()
	cur = db.execute('select * from assignments')
	entries = cur.fetchall()
	for assignment in entries:
		assignment_list.append(Assignment(
			assignment['a_id'], assignment['a_name'], assignment['a_active']))
	return assignment_list

#Gets all problems in the database
def get_db_problems():
	problem_list = []
	db = get_db()
	cur = db.execute('select * from problems')
	entries = cur.fetchall()
	for problem in entries:
		problem_list.append(Problem(
			problem['p_id'], problem['a_id'], problem['p_name'], problem['p_desc'], problem['p_solution_name']))
	return problem_list

#Gets a specific problem in the database determined by it's ID
def get_single_problem(problem_id):
	db = get_db()
	cur = db.execute(
		'select * from problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	problem = Problem(entry['p_id'], entry['a_id'], entry['p_name'],
					  entry['p_desc'], entry['p_solution_name'])
	return problem


def get_function_name(problem_id):
	db = get_db()
	cur = db.execute(
		'select P.p_solution_name from Problems P where P.p_id = {}'.format(problem_id))
	entry = cur.fetchone()
	return entry['p_solution_name']

#Inserts a new problem into the db
def insert_problem(assignment_id, problem_name, problem_desc, problem_solution_name):
	params = (assignment_id, problem_name, problem_desc, problem_solution_name)
	db = get_db()
	db.execute(
		'insert into problems(a_id, p_name, p_desc, p_solution_name) VALUES (?,?,?,?)', params)
	db.commit()

#Gets the highest current Problem ID, so the one inserted to the DB will come after that one
def get_max_problem_id():
	db = get_db()
	cur = db.execute('select MAX(p_id) from problems')
	entry = cur.fetchone()
	return entry['MAX(p_id)']
	