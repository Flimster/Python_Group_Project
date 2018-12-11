import os
from flask import current_app as app
from werkzeug.utils import secure_filename
from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for

upload = Blueprint('/upload', __name__)

UPLOAD_FOLDER = './uploads/python'
ALLOWED_EXTENSIONS = set(['py'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

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