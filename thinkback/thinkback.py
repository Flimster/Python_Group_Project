from pathlib import Path
from subprocess import call
from flask import Flask, render_template, request
from .models import Project
from .views import about, assignments

app = Flask(__name__)

app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignments_blueprint)

# Create a project with 10 empty problems
project1 = Project()
for i in range(10):
	project1.create_problem()

@app.route('/')
def index():
    return render_template('/index.html', value=project1)
	
@app.route('/problem/<problem_name>', methods=['GET'])
def problem_description(problem_name):
	return "Hello world this is problem {}".format(problem_name)

@app.route('/upload/<problem_name>', methods=['POST'])
def upload_sum_problem(problem_name):
	print(problem_name)
	# if request.method == 'POST':
	# 	p = Path('.')
	# 	file_uploaded = request.files['myfile'].read().decode()
	# 	for file in p.glob('./tests/impl.py'):
	# 		with open(file, 'w') as f:
	# 			f.write(file_uploaded)
	# call(["pytest", "-q"]) 
	return "Success"


if __name__ == '__main__':
    app.run(debug=True)
