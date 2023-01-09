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

def get_adv_by_email(email) -> SalesAdv:
    return SalesAdv.query.filter(SalesAdv.email == email).first()

def get_rep_by_email(email) -> SalesRep:
    return SalesRep.query.filter(SalesRep.email == email).first()

def get_relationships_by_adv_id(adv_id):
    return AdvRep.query.filter(AdvRep.adv_id == adv_id).all()

def get_rep_by_relationship_id(adv_rep) -> SalesRep:
    return SalesRep.query.filter(SalesRep.rep_id == adv_rep.rep_id)

def get_relationships_by_rep_id(rep_id):
    return AdvRep.query.filter(AdvRep.rep_id == rep_id)

def get_rep_by_rep_id(rep_id):
    return SalesRep.query.filter(SalesRep.rep_id == rep_id).first()

def get_adv_by_adv_id(adv_id):
    return SalesAdv.query.filter(SalesAdv.adv_id == adv_id).first()
    

def get_messages_by_adv_id(adv_id):
    return Messages.query.filter(Messages.adv_id == adv_id).all()