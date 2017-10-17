from flask import request
from flask import Flask
app=Flask(__name__)

@app.route('/')
def index():
	user_agent=request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent

@app.route('/usr/<name>')
def user(name):
	return '<h1>Hello,%s~</h1>' % name

@app.route('/usr/<name>/profile')
def usr(name):
	return '<h1>this is my profile:my name is %s.</h1>' % name

if __name__=='__main__':
	app.run(debug=True)

