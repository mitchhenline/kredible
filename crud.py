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
    adv_rep = AdvRep.query.filter(AdvRep.adv_id == adv_id)
    print(type(adv_rep)) 
    return adv_rep #this will display the AdvRep ids but I cannot get the name to display

def get_relationships_by_rep_id(rep_id):
    adv_rep = AdvRep.query.filter(AdvRep.rep_id == rep_id)
    print(type(adv_rep)) 
    return adv_rep

def get_rep_by_rep_id(rep_id):
    rep = SalesRep.query.filter(SalesRep.rep_id == rep_id).first()

def get_adv_by_adv_id(adv_id):
    rep = SalesAdv.query.filter(SalesAdv.adv_id == adv_id).first()


    # rep_id_name = relationship.rep_id
    # return relationship

# def get_concerts(email: str):
#     user = get_user_by_email(email)
#     return Concert.query.filter(Concert.user_id == user.user_id)