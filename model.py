"""Models for Kredible app"""

import os, datetime
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import func

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
    phone_number = db.Column(db.String(20))

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
    phone_number = db.Column(db.String)
    availability = db.Column(db.Text)

    def __repr__(self):
        return f'User: adv_id={self.adv_id} Name={self.last_name, self.first_name} Company={self.company}'

class Customer(db.Model):
    """Potential customers of the sales representatives. Not a site user, intended to be primarily information."""

    __tablename__ = "customers"

    cust_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    company = db.Column(db.String(255))
    phone_number = db.Column(db.String)
    notes = db.Column(db.Text)
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
    time = db.Column(db.String)  #change to time later, can't pass in the right format with DateTime(timezone=True), server_default=func.now()
    meeting_link = db.Column(db.String(255))
    meeting_prep_notes = db.Column(db.Text)
    meeting_accepted = db.Column(db.Boolean, default=False)
    cust_id = db.Column(db.Integer, db.ForeignKey("customers.cust_id"))
    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"))
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"))


    sales_rep = db.relationship("SalesRep", backref="meetings")
    sales_adv = db.relationship("SalesAdv", backref="meetings")
    customer = db.relationship("Customer", backref="meetings")

class Messages(db.Model):
    """Messages table"""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    datetime_created = db.Column(db.DateTime, default=datetime.now())
    content = db.Column(db.String(255), nullable=False)

    adv_id = db.Column(db.Integer, db.ForeignKey("sales_advs.adv_id"), nullable=False)
    rep_id = db.Column(db.Integer, db.ForeignKey("sales_reps.rep_id"), nullable=False)

    sales_rep = db.relationship("SalesRep", backref="messages")
    sales_adv = db.relationship("SalesAdv", backref="messages")

def connect_to_db(flask_app, db_uri=os.environ["POSTGRES_URI"], echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Database connected.")

if __name__ == "__main__":
    from server import app
    connect_to_db(app)