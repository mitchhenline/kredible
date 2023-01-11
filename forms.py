from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, DateField, TimeField, SelectField

class AdvLoginForm(FlaskForm):
    email = StringField('Email ', [validators.InputRequired()])
    password = PasswordField('Password ', [validators.InputRequired()])

class RepLoginForm(FlaskForm):
    email = StringField('Email ', [validators.InputRequired()])
    password = PasswordField('Password ', [validators.InputRequired()])

class AddCustomer(FlaskForm):
    first_name=StringField('First Name ', [validators.InputRequired()])
    last_name=StringField('Last Name ', [validators.InputRequired()])
    email=StringField('Email ', [validators.InputRequired()])
    company=StringField('Company ', [validators.InputRequired()])
    phone_number=StringField('Phone Number ')
    notes=TextAreaField('Notes ')

class RequestMeeting(FlaskForm):
    date=DateField('Date ')
    time=TimeField('Time ')
    meeting_link=StringField('Meeting link ', [validators.InputRequired()])
    meeting_prep_notes=TextAreaField('Meeting Notes ')
    cust_id=SelectField('Customer ', [validators.DataRequired()])
    