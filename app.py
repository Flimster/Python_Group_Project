from pathlib import Path
from subprocess import call
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'The about page'

@app.route('/file', methods=['POST'])
def upload_file():
	if request.method == 'POST':
		p = Path('.')
		tmp = request.files['myfile'].read().decode()
		for file in p.glob('./tests/impl.py'):
			with open(file, 'w') as f:
				f.write(tmp)
	call(["pytest", "-q"]) 
	return "Success"

if __name__ == '__main__':
    app.run(debug=True)
