# thinkback/views/assignments.py
import os
import json
import sqlite3
import importlib
from flask import current_app as app
from werkzeug.utils import secure_filename
from ..models import Assignment, Problem, ProblemModule
from flask import Blueprint, render_template, request, redirect, flash, url_for, g

ALLOWED_EXTENSIONS = set(['py'])

assignment_blueprint = Blueprint('/assignments', __name__)

@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
	assignment_list = get_db_assignments()
	problem_list = get_db_problems()
	for assignment in assignment_list:
		for problem in problem_list:
			if problem.assignment_id == assignment.id:
				assignment.problem_list.append(problem)

	if link == 'active_assignments':
		return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 1))
	if link == 'past_assignments':
		return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 0))
	return "Something went wrong"


@assignment_blueprint.route('/<link>/<problem_id>', methods=['GET'])
def get_problems(link, problem_id):
	problem = get_single_problem(problem_id)
	return render_template('problem.html', link=link, problem=problem, results={})



def filter_assignments(assignments, status):
	filtered_assignment_list = []
	for assignment in assignments:
		if assignment.active == status:
			filtered_assignment_list.append(assignment)
	return filtered_assignment_list


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

def connect_db():
	print("""Connects to the specific database.""")
	rv = sqlite3.connect(app.config['DATABASE'])
	rv.row_factory = sqlite3.Row
	return rv


def get_db():
	print("""Opens a new database connection if there is none yet for the
	current application context.
	""")
	if not hasattr(g, 'thinkback.db'):
		g.sqlite_db = connect_db()
	return g.sqlite_db
