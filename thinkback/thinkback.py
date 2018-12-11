import os
from pathlib import Path
from flask import Flask, render_template
from .views import about, assignments, upload



app = Flask(__name__)
app.secret_key = b'super secret key'


app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)
app.register_blueprint(upload.upload)

@app.route('/index')
@app.route('/')
def index():
	return render_template('/index.html')

if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)
