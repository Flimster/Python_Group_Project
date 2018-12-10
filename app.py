from pathlib import Path
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
		print('The method was a post method')
		tmp = request.files['myfile'].read().decode()
		print(type(tmp))
		for file in p.glob('./tests/impl.py'):
			with open(file, 'w') as f:
				f.write(tmp)
	return "Success"

if __name__ == '__main__':
    app.run(debug=True)
