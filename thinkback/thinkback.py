import os
from pathlib import Path
from subprocess import call
from .views import about, assignments
from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, flash, redirect, url_for

UPLOAD_FOLDER = './uploads/python'
ALLOWED_EXTENSIONS = set(['py'])

app = Flask(__name__)
app.secret_key = b'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)

@app.route('/index')
@app.route('/')
def index():
	return render_template('/index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		# Check if the post request has a file in it
		if 'file' not in request.files:
			return redirect(request.url)

		file = request.files['file']
		if file.filename == '':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			return url_for('get_active_assignments')
	return ""

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)
