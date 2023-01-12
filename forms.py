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
    time=StringField('Time ')
    # time=TimeField('Time ', format='%I:%M:%p') format I had that isn't working
    meeting_link=StringField('Meeting link ', [validators.InputRequired()])
    meeting_prep_notes=TextAreaField('Meeting Notes ')
    cust_id=SelectField('Customer ', choices=[('2',"Adam Lazarra"), ('3', "Taylor Swift")])



# ------select field isn't populating choices-------
# this is what needs to go in the [] in line 25
# choices=[('option1', 'Option 1'), ('option2', 'Option 2'), ('option3', 'Option 3')])
# first element is value, second element is what will be displayed
# will need to look like ths
# ('customers.cust_id', 'customers.first_name customers.last_name')
    