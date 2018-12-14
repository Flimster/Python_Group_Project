# thinkback/views/assignments.py
from ..database import database
from flask import current_app as app
from flask import Blueprint, render_template
from ..models import Assignment, Problem, ProblemModule

assignment_blueprint = Blueprint('/assignments', __name__)

@assignment_blueprint.route('/<link>', methods=['GET'])
def get_assignment_path(link):
    assignment_list = database.get_db_assignments()
    problem_list = database.get_db_problems()
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
    problem = database.get_single_problem(problem_id)
    return render_template('problem.html', link=link, problem=problem, results={})


def filter_assignments(assignments, status):
    filtered_assignment_list = []
    for assignment in assignments:
        if assignment.active == status:
            filtered_assignment_list.append(assignment)
    return filtered_assignment_list
