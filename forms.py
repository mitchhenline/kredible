from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, IntegerField

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
    phone_number=IntegerField('Phone Number ')