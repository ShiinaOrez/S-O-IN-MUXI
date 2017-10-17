from flask import Flask
from flask import render_template
app=Flask(__name__)

@app.route('/')
def index():
	comments=['kaga','fubuki']
	return render_template('test.html',comments=comments)
if __name__=='__main__':
	app.run(debug=True)
