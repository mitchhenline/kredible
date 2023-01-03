"""Models for Kredible app"""

import os, datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SalesRep(db.Model):
    """A sales representative site user"""

    __tablename__ = "sales_reps"

    rep_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    company = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)

    def __repr__(self):
        return f'User: rep_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'

class SalesAdv(db.Model):
    """A sales advocate site user"""

    __tablename__ = "sales_advs"

    adv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    company = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)

    def __repr__(self):
        return f'User: adv_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'

class Customer(db.Model):
    """Potential customers of the sales representatives. Not a site user, intended to be primarily information."""

    __tablename__ = "customers"

    cust_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    company = db.Column(db.String(255))
    phone_number = db.Column(db.Integer)
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))

    sales_rep = db.relationship("SalesRep", backref="customers")

    def __repr__(self):
        return f'User: cust_id={self.rep_id} Name={self.last_name, self.first_name} Company={self.company}'

class AdvRep(db.Model):
    """Advocate-Representative relationship table"""

    __tablename__ = "adv_rep_relationships"

    adv_rep = db.Column(db.Integer, autoincrement=True, primary_key=True)
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))
    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"))

    sales_rep = db.relationship("SalesRep", backref="adv_rep_relationships")
    sales_adv = db.relationship("SalesAdv", backref="adv_rep_relationships")

class Meeting(db.Model):
    """Meeting table"""

    __tablename__ = "meetings"

    meeting_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    meeting_link = db.Column(db.String(255))
    cust_id = db.Column(db.Integer, db.ForeignKey("customers.rep_id"))
    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"))
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))

    sales_rep = db.relationship("SalesRep", backref="meetings")
    sales_adv = db.relationship("SalesAdv", backref="meetings")
    customer = db.relationship("Customer", backref="meetings")

class Messages(db.Model):
    """Messages table"""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime)
    message = db.Column(db.Text(5000))
    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"))
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))

    sales_rep = db.relationship("SalesRep", backref="messages")
    sales_adv = db.relationship("SalesAdv", backref="messages")

class Calendar(db.Model):
    """Sales advocate availability calendar"""

    __tablename__ = "calendar"

    cal_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sunday = db.Column(db.String)
    monday = db.Column(db.String)
    tuesday = db.Column(db.String)
    wednesday = db.Column(db.String)
    thursday = db.Column(db.String)
    friday = db.Column(db.String)
    saturday = db.Column(db.String)
    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"))

    sales_adv = db.relationship("SalesAdv", backref="calendar")

