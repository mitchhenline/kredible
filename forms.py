from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, TextAreaField, DateField, TimeField, SelectField, SubmitField
from model import Customer, SalesRep, SalesAdv

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
    company_size=SelectField('Company Size ', choices = [("Small", "Small"), ("Commercial", "Commercial"), ("Enterprise", "Enterprise")])
    region=SelectField('Region ', choices = ["Midwest","Mountain","Northeast","Pacific","South"])
    industry=SelectField('Industry ', choices = ["Automobiles & Components", "Banks", "Capital Goods", "Commercial & Professional Service", "Education", "Energy", "Food, Beverage & Tobacco", "Government", "Heathcare", "Retail" ])
    phone_number=StringField('Phone Number ')
    notes=TextAreaField('Notes ')


def MeetingFunc(rep_id):
    time_choices = [("8:00 AM", "8:00 AM"), ("8:15 AM", "8:15 AM"), ("8:30 AM", "8:30 AM"), ("8:45 AM", "8:45 AM"), ("9:00 AM", "9:00 AM"), ("9:15 AM", "9:15 AM"), ("9:30 AM", "9:30 AM"), ("9:45 AM", "9:45 AM"), ("10:00 AM", "10:00 AM"), ("10:15 AM", "10:15 AM"), ("10:30 AM", "10:30 AM"), ("10:45 AM", "10:45 AM"), ("11:00 AM", "11:00 AM"), ("11:15 AM", "11:15 AM"), ("11:30 AM", "11:30 AM"), ("11:45 AM", "11:45 AM"), ("12:00 PM", "12:00 PM"), ("12:15 PM", "12:15 PM"), ("12:30 PM", "12:30 PM"), ("12:45 PM", "12:45 PM"), ("1:00 PM", "1:00 PM"), ("1:15 PM", "1:15 PM"),("1:30 PM", "1:30 PM"), ("1:45 PM", "1:45 PM"), ("2:00 PM", "2:00 PM"), ("2:15 PM", "2:15 PM"),("2:30 PM", "2:30 PM"), ("2:45 PM", "2:45 PM"), ("3:00 PM", "3:00 PM"), ("3:15 PM", "3:15 PM"),("3:30 PM", "3:30 PM"), ("3:45 PM", "3:45 PM"), ("4:00 PM", "4:00 PM"), ("4:15 PM", "4:15 PM"),("4:30 PM", "4:30 PM"), ("4:45 PM", "4:45 PM"), ("5:00 PM", "5:00 PM"), ("5:15 PM", "5:15 PM"),("5:30 PM", "5:30 PM"), ("5:45 PM", "5:45 PM"), ("6:00 PM", "6:00 PM")]
    class RequestMeeting(FlaskForm):
        date=DateField('Date ')
        time=SelectField('Time ', choices = time_choices)
        meeting_link=StringField('Meeting link ', [validators.InputRequired()])
        meeting_prep_notes=TextAreaField('Meeting Notes ')
        choices = [ (c.cust_id, c.first_name +" "+ c.last_name) for c in Customer.query.filter_by(rep_id = rep_id).all()]
        cust_id=SelectField('Customer ', choices=choices)
    return RequestMeeting()

# def MeetingFuncCust(rep_id):
#     class RequestMeetingCust(FlaskForm):
#         date=DateField('Date ')
#         time=StringField('Time ')
#         # time=TimeField('Time ', format='%I:%M:%p') format I had that isn't working
#         meeting_link=StringField('Meeting link ', [validators.InputRequired()])
#         meeting_prep_notes=TextAreaField('Meeting Notes ')
#         choices = [ (c.adv_id, c.first_name +" "+ c.last_name) for c in SalesAdv.query.filter_by(sales_rep['rep_id'] == rep_id).all()]
#         adv_id=SelectField('Advocate ', choices=choices)
#     return RequestMeetingCust()           ######choices line is holding this function back####

class AcceptMeeting(FlaskForm):
    meeting_accepted=SubmitField('Accept')

