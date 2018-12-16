# thinkback/views/assignments.py

from ..database import database
from flask import current_app as app
from ..models import Assignment, Problem
from flask import Blueprint, render_template

assignment_blueprint = Blueprint('/assignments', __name__)

@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    """Gets the path of active/past assignments"""
    assignment_list = database.get_assignments_with_problems()
    if link == 'active_assignments':
        return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 1), flag=True)
    elif link == 'past_assignments':
        return render_template('assignments.html', assignment_list=filter_assignments(assignment_list, 0), flag=False)
    elif link.isdigit() and int(link) <= len(assignment_list):
        return render_template('createassignment.html', assignment_id=link)
    return render_template("404.html")

@assignment_blueprint.route('/<link>/<problem_id>', methods=['GET'])
def get_problems(link, problem_id):
    """Gets the problem for a specific assignment"""
    problem = database.get_single_problem(problem_id)
    return render_template('problem.html', link=link, problem=problem)

@assignment_blueprint.route('/<assignment_id>', methods=['GET'])
def create_assignment(assignment_id):
    """Directs the user to a createassignment page"""
    return render_template('createassignment.html', assignment_id=assignment_id)


def filter_assignments(assignments, status):
    """Filters the assignments according to it's status"""
    filtered_assignment_list = []
    for assignment in assignments:
        if assignment.active == status:
            filtered_assignment_list.append(assignment)
    return filtered_assignment_list