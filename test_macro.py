from flask import Flask 
from flask import render_template
app=Flask(__name__)

@app.route('/user/shiina_orez')
def shiina_orez():
	comments=['kaga','fubuki']
	return render_template('macro.html',comments=comments)

if __name__=='__main__':
	app.run(debug=True)
