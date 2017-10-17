from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField,SubmitField
from wtforms.validators import Required,Email
app=Flask(__name__)

bootstrap=Bootstrap(app)

app.config['SECRET_KEY']='mashiro'

@app.route('/',methods=['GET','POST'])
def index():
	form=NameForm()
	if form.validate_on_submit():
		old_name=session.get('name')
		if old_name is not None and old_name != form.name.data:
			flash('looks like you have changed your name!')
		session['name']=form.name.data
		return redirect(url_for('index'))
	return render_template('index.html',form=form,name=session.get('name'))

@app.route('/email',methods=['GET','POST'])
def email():
	form=emailform()
	if form.validate_on_submit():
		old_email=session.get('email')
		if old_email is not None and old_email != form.email.data:
			flash('are you sure?it is diffrent with before!')
		session['email']=form.email.data
		return redirect(url_for('email'))
	return render_template('email.html',form=form,email=session.get('email'))

@app.route('/war_ship/BBBC')
def BBBC():
	return render_template('BBBC.html')

@app.errorhandler(404)
def page_not_found(e):
	return render_template('404.html'),404

class emailform(Form):
	email=StringField('what is your email?',validators=[Email()])
	submit=SubmitField('Submit')

class NameForm(Form):
	name=StringField('what is your name?',validators=[Required()])
	submit=SubmitField('Submit')

if __name__== '__main__':
	app.run(debug=True)
