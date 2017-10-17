from flask import Flask
from flask import render_template
from flask_wtf import Form
from wtforms.fields import (StringField, PasswordField, DateField, BooleanField,
                            SelectField, SelectMultipleField, TextAreaField,
                            RadioField, IntegerField, DecimalField, SubmitField)
from wtforms.validators import DataRequired, Length, Email, EqualTo, NumberRange
app=Flask(__name__)
app.config['SECRET_KEY']='mashiro'
 
class RegisterForm(Form):
    
    username = StringField('Username', validators=[Length(min=4, max=25)])
 
    
    email = StringField('Email Address', validators=[Email()])
 
    
    password = PasswordField('Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
 
    
    confirm = PasswordField('Repeat Password')
 
    
    age = IntegerField('Age', validators=[NumberRange(min=16, max=70)])
 
    
    height = DecimalField('Height (Centimeter)', places=1)
 
    
    birthday = DateField('Birthday', format='%Y-%m-%d')
 
    
    gender = RadioField('Gender', choices=[('m', 'Male'), ('f', 'Female')],
                                  validators=[DataRequired()])
 
    
    job = SelectField('Job', choices=[
        ('teacher', 'Teacher'),
        ('doctor', 'Doctor'),
        ('engineer', 'Engineer'),
        ('lawyer', 'Lawyer')
    ])
 
    
    hobby = SelectMultipleField('Hobby', choices=[
        ('swim', 'Swimming'),
        ('skate', 'Skating'),
        ('hike', 'Hiking')
    ])
 
    
    description = TextAreaField('Introduction of yourself')
 
    
    accept_terms = BooleanField('I accept the Terms of Use', default='checked',
                                validators=[DataRequired()])
 
    
    submit = SubmitField('Register')

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash('User "%s" registered successfully! Please login.' % form.username.data)
        login_form = LoginForm()
        return render_template('login.html', form=login_form)
 
    return render_template('register.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
