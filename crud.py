"""CRUD operations"""
from model import db, User, Customer, AdvRep, Meeting, Messages, Calendar

def create_user(is_adv, email, password, first_name, last_name, company, phone_number):
    user = User(
        is_adv=is_adv,
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        company=company,
        phone_number=phone_number)
    return user

def get_user_by_email(email):
    pass