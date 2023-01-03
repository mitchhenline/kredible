"""Models for Kredible app"""

import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SalesRep(db.Model):
    """A sales representative user"""

    __tablename__ = "sales_reps"

    rep_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company = db.Column(db.String)
    phone_number = db.Column(db.Integer)

    def __repr__(self):
        return f'User: rep_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'

class SalesAdv(db.Model):
    """A sales advocate user"""

    __tablename__ = "sales_advs"

    adv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    company = db.Column(db.String)
    phone_number = db.Column(db.Integer)

    def __repr__(self):
        return f'User: adv_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'

class Customer(db.Model):
    """Potential customers of the sales representatives"""

    __tablename__ = "potential_customers"

    cust_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    company = db.Column(db.String)
    phone_number = db.Column(db.Integer)
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))
    sales_rep = db.relationship("SalesRep", backref="potential_customers")

    def __repr__(self):
        return f'User: cust_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'