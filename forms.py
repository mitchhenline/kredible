from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, DateField, TimeField, SelectField, BooleanField
from model import Customer

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

def MeetingFunc(rep_id):
    class RequestMeeting(FlaskForm):
        date=DateField('Date ')
        time=StringField('Time ')
        # time=TimeField('Time ', format='%I:%M:%p') format I had that isn't working
        meeting_link=StringField('Meeting link ', [validators.InputRequired()])
        meeting_prep_notes=TextAreaField('Meeting Notes ')
        choices = [ (c.cust_id, c.first_name +" "+ c.last_name) for c in Customer.query.filter_by(rep_id = rep_id).all()]
        cust_id=SelectField('Customer ', choices=choices)
    return RequestMeeting()

class AcceptMeeting(FlaskForm):
    meeting_accepted=BooleanField('Accept')
