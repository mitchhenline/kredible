"""CRUD operations"""
from model import db, SalesAdv, SalesRep, Customer, AdvRep, Meeting, Messages, Calendar

def create_sales_rep(email, password, first_name, last_name, company, phone_number):
    sales_rep = SalesRep(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        company=company,
        phone_number=phone_number)
    return sales_rep

def create_sales_adv(email, password, first_name, last_name, company, phone_number):
    sales_adv = SalesAdv(
        email=email,
        password=password,
        first_name=first_name,
        last_name=last_name,
        company=company,
        phone_number=phone_number)
    return sales_adv

def get_user_by_email(email):
    pass