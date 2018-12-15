# thinkback/views/assignments.py
from ..database import database
from flask import current_app as app
from flask import Blueprint, render_template
from ..models import Assignment, Problem

assignment_blueprint = Blueprint('/assignments', __name__)

@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
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
    problem = database.get_single_problem(problem_id)
    return render_template('problem.html', link=link, problem=problem)

@assignment_blueprint.route('/<assignment_id>', methods=['GET'])
def create_assignment(assignment_id):
    return render_template('createassignment.html', assignment_id=assignment_id)


def filter_assignments(assignments, status):
    filtered_assignment_list = []
    for assignment in assignments:
        if assignment.active == status:
            filtered_assignment_list.append(assignment)
    return filtered_assignment_list