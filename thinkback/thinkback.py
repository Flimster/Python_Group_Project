from flask import Flask, render_template
from .views import about, assignments

UPLOAD_FOLDER = './uploads'

app = Flask(__name__)
app.secret_key = b'super secret key'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.register_blueprint(about.about_blueprint)
app.register_blueprint(assignments.assignment_blueprint)

@app.route('/index')
@app.route('/')
def index():
	return render_template('/index.html')

if __name__ == '__main__':
	app.config['SESSION_TYPE'] = 'filesystem'
	app.run(debug=True)