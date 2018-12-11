from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/active_assignments')
def active_assignments():
    return 'active_assignments'

@app.route('/past_assignments')
def get_past_assignments():
    return 'past_assignments'

@app.route('/past_assignment/<assignments>')
def get_past_problems():
    return 'past_problems'
with app.test_request_context():
    print(url_for('index'))
    print(url_for('active_assignments'))
    print(url_for('past_assignments'))